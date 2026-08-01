# Job Search Agent (Priority)

Finds best-fit job openings from your resume, ranks them, and (in later phases) drafts applications with human approval before submit.

## Status

| Phase | Feature | Status |
|-------|---------|--------|
| 1 | Resume load + keyword/LLM match | **Done (MVP)** |
| 2 | Live job APIs | Planned |
| 3 | Cover letter draft | Planned |
| 4 | Human-in-the-loop apply | Planned |

## Quick start

```bash
source .venv/bin/activate  # from repo root
pip install -r requirements.txt

python -m agents.job_search.src.cli \
  --resume ../../resume-output/Umesh_Chandra_PV_ATS_Resume_DevOps_SRE_AI.txt
```

## Architecture

```
resume.txt → [load] → [fetch jobs] → [score] → ranked report
```

Implemented with LangGraph in `src/graph.py`. Demo jobs ship in `data/sample_jobs.json`.

## Target roles (from resume)

DevOps Engineer, SRE, AI Platform Engineer — Hyderabad / remote India-friendly.

## Environment

Copy `.env.example` to `.env` and set `OPENAI_API_KEY` for LLM scoring (optional).
