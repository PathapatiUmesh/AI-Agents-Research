# Getting Started — AI Agents Research

Welcome. This repo is organized as **one folder per agent**, grouped by category. Your priority agent is **job-search**; everything else is scaffolded for later.

## Your profile (from repo context)

You have **6+ years** in DevOps / SRE / AI Platform engineering (Python, Kubernetes, AWS/Azure/GCP, CI/CD, observability). You are pivoting toward **AI Engineer** and **AI Solutions Architect** roles. That background is a strong fit for building production agents — you already think in reliability, automation, and platform design.

## Framework recommendation

| Framework | Best for | Use in this repo |
|-----------|----------|------------------|
| **LangGraph** (recommended primary) | Stateful workflows, checkpoints, human-in-the-loop, production pipelines | **Job-search agent** (resume → fetch → score → approve → apply) |
| **LangChain** | Tools, retrievers, LLM integrations | Shared layer under LangGraph nodes |
| **CrewAI** | Role-based teams (“researcher”, “writer”, “reviewer”) | Research & Data agents later |
| **AutoGen** | Multi-agent chat + code execution | Software Engineering agents (bug-fix, tests) later |

**Why LangGraph first for you**

1. Your job-search agent is a **pipeline with state**, not a single chat turn (parse resume → find jobs → score → draft cover letter → **human approves** → submit).
2. You need **human-in-the-loop** before auto-apply (legal, ToS, and quality).
3. LangGraph maps cleanly to how you already build systems: nodes, edges, observability, retries.
4. You know **Python + FastAPI** — LangGraph fits your stack.

Use **CrewAI** when you add the Research agents (web reports, financial docs). Use **AutoGen** when agents need to run code in a sandbox (refactoring, unit tests).

## What I still need from you (experience questionnaire)

Answer these so we can tune complexity and tooling:

1. **LLM usage** — Have you called OpenAI/Anthropic/Azure OpenAI APIs from Python? Used prompt templates or structured output (Pydantic)?
2. **RAG** — Built anything with embeddings + vector DB (Chroma, Pinecone, pgvector)?
3. **Agent frameworks** — Tried LangChain, LangGraph, CrewAI, or AutoGen before? Which?
4. **Web automation** — Comfortable with Playwright/Selenium for form fill? (needed for apply phase)
5. **Time budget** — Hours per week for this project?
6. **Job boards** — Which sites do you target? (LinkedIn, Naukri, Indeed, company career pages — affects legal/technical approach)
7. **API budget** — Monthly spend cap for LLM + job APIs?
8. **Auto-apply comfort** — Fully automated vs. “agent prepares, I click submit”?

Until you answer, we assume: **strong Python/DevOps**, **new to agent frameworks**, **human approval before any apply**.

## Recommended project to build **today**

### Day 1: Resume Match MVP (`agents/job-search`)

**Goal:** Given your resume, produce a **ranked list of job matches** with scores and reasons. No auto-apply yet.

**Why this first**

- Uses your real resume already in `resume-output/`
- Teaches agent **state**, **tools**, and **structured output**
- Delivers immediate job-search value
- Safe and legal (read-only)

**Steps**

```bash
cd /workspace
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Demo mode (no API key) — keyword matching
python agents/job-search/run.py \
  --resume resume-output/Umesh_Chandra_PV_ATS_Resume_DevOps_SRE_AI.txt

# With LLM scoring (set OPENAI_API_KEY in .env)
python agents/job-search/run.py \
  --resume resume-output/Umesh_Chandra_PV_ATS_Resume_DevOps_SRE_AI.txt \
  --use-llm
```

**Day 2–3:** Wire a job API (Adzuna, JSearch, or SerpAPI Google Jobs).

**Week 2:** LangGraph node for **draft cover letter** + approval UI (CLI or simple FastAPI).

**Week 3+:** Playwright apply flow **only** on sites you own or that allow automation, with you in the loop.

## Roadmap by agent

| Phase | Agent | Milestone |
|-------|-------|-----------|
| 1 | `job-search` | Match + rank (today) |
| 2 | `job-search` | Live job feed + daily digest |
| 3 | `job-search` | Draft application + human approve |
| 4 | `software-engineering/bug-fix` | Repo-aware bug triage agent |
| 5 | `customer-operations/support-tickets` | Ticket classify + route |
| 6 | `research-data/web-reports` | CrewAI research crew |

## Career path note (AI Engineer → Solutions Architect)

- **AI Engineer:** Ship agents that work reliably (evals, logging, retries, cost controls).
- **Solutions Architect:** Design *which* agents, *what* data flows, *where* human gates sit, and *how* systems integrate (ATS, CRM, observability).

This repo is structured so each folder becomes a **portfolio piece** with README, tests, and a demo command.
