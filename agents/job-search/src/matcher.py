from __future__ import annotations

import os
import re

from .models import AgentState, JobMatch, JobPosting


def score_jobs(state: AgentState) -> list[JobMatch]:
    if state.use_llm and os.getenv("OPENAI_API_KEY"):
        return _score_with_llm(state)
    return [_score_keyword(job, state) for job in state.jobs]


def _score_keyword(job: JobPosting, state: AgentState) -> JobMatch:
    blob = f"{job.title} {job.description} {job.location}".lower()
    reasons: list[str] = []
    missing: list[str] = []

    role_hits = sum(1 for role in state.target_roles if _role_matches(role, blob, job.title))
    skill_hits = [s for s in state.skills if s in blob]
    for skill in state.skills:
        if skill not in blob:
            missing.append(skill)

    score = 0.0
    if role_hits:
        score += min(40, role_hits * 20)
        reasons.append(f"Title/role alignment ({role_hits} target role hit(s))")

    if skill_hits:
        skill_pct = len(skill_hits) / max(len(state.skills), 1)
        score += skill_pct * 50
        reasons.append(f"Skill overlap: {', '.join(skill_hits[:8])}")

    if "hyderabad" in blob or "bangalore" in blob or "remote" in blob.lower():
        score += 10
        reasons.append("Location preference match (India / remote)")

    # Penalize obvious mismatches
    if "frontend" in blob and "react" in blob and "kubernetes" not in blob:
        score = min(score, 25)
        reasons.append("Likely role mismatch (frontend-focused)")

    score = round(min(100, max(0, score)), 1)
    if not reasons:
        reasons.append("Low overlap with resume keywords")

    return JobMatch(
        job=job,
        score=score,
        reasons=reasons,
        missing_skills=missing[:5],
    )


def _role_matches(role: str, blob: str, title: str) -> bool:
    title_l = title.lower()
    if role in title_l or role in blob:
        return True
    if role == "sre" and "site reliability" in blob:
        return True
    return False


def _score_with_llm(state: AgentState) -> list[JobMatch]:
    try:
        from langchain_core.prompts import ChatPromptTemplate
        from langchain_openai import ChatOpenAI
        from pydantic import BaseModel, Field
    except ImportError as exc:
        raise RuntimeError("Install requirements.txt for LLM scoring") from exc

    class MatchResult(BaseModel):
        score: float = Field(ge=0, le=100)
        reasons: list[str]
        missing_skills: list[str] = Field(default_factory=list)

    llm = ChatOpenAI(model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"), temperature=0)
    structured = llm.with_structured_output(MatchResult)
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You score job fit for a candidate. Be strict; only high scores for strong DevOps/SRE/AI Platform fit.",
            ),
            (
                "human",
                "Resume excerpt (skills/roles):\n{resume}\n\nJob:\nTitle: {title}\nCompany: {company}\n"
                "Location: {location}\nDescription: {description}",
            ),
        ]
    )
    chain = prompt | structured

    matches: list[JobMatch] = []
    resume_excerpt = state.resume_text[:4000]
    for job in state.jobs:
        result: MatchResult = chain.invoke(
            {
                "resume": resume_excerpt,
                "title": job.title,
                "company": job.company,
                "location": job.location,
                "description": job.description,
            }
        )
        matches.append(
            JobMatch(
                job=job,
                score=result.score,
                reasons=result.reasons,
                missing_skills=result.missing_skills,
            )
        )
    return matches
