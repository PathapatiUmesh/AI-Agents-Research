# AI-Agents-Research

A portfolio of **AI agents**, one folder per agent, organized by category. Priority: **job-search** — find best-fit roles from your resume (auto-apply with human approval in later phases).

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Run job-search agent (demo jobs, keyword scoring)
python agents/job-search/run.py \
  --resume resume-output/Umesh_Chandra_PV_ATS_Resume_DevOps_SRE_AI.txt
```

See **[docs/GETTING_STARTED.md](docs/GETTING_STARTED.md)** for framework recommendations, career roadmap, and what to build today.

## Repository layout

```
agents/
  job-search/              # PRIORITY — resume → match → rank (LangGraph)
  software-engineering/
    bug-fix/
    unit-tests/
    refactoring/
  customer-operations/
    support-tickets/
    data-routing/
    multi-step-requests/
  research-data/
    web-reports/
    financial-analysis/
    market-monitoring/
docs/
  GETTING_STARTED.md
  FRAMEWORK_GUIDE.md
resume-output/             # Your ATS resume (PDF + TXT)
```

## Tests

```bash
source .venv/bin/activate
pytest agents/job-search/tests/ -q
```

## Framework choice

**LangGraph** for the job-search pipeline (stateful, human-in-the-loop ready). **CrewAI** planned for research agents. **AutoGen** planned for code-focused software engineering agents.

Details: [docs/FRAMEWORK_GUIDE.md](docs/FRAMEWORK_GUIDE.md)
