from __future__ import annotations

from pydantic import BaseModel, Field


class JobPosting(BaseModel):
    id: str
    title: str
    company: str
    location: str
    url: str
    description: str


class JobMatch(BaseModel):
    job: JobPosting
    score: float = Field(ge=0, le=100)
    reasons: list[str]
    missing_skills: list[str] = Field(default_factory=list)


class AgentState(BaseModel):
    resume_path: str
    resume_text: str = ""
    target_roles: list[str] = Field(default_factory=list)
    skills: list[str] = Field(default_factory=list)
    jobs: list[JobPosting] = Field(default_factory=list)
    matches: list[JobMatch] = Field(default_factory=list)
    use_llm: bool = False
