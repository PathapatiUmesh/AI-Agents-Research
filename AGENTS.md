# AGENTS.md

Guidance for AI agents working in this repository.

## Cursor Cloud specific instructions

### Services

| Service | Required | How to start | Notes |
|---------|----------|--------------|-------|
| Job-search agent (CLI) | For job-search work | `source .venv/bin/activate && python agents/job-search/run.py --resume resume-output/Umesh_Chandra_PV_ATS_Resume_DevOps_SRE_AI.txt` | No long-running server; one-shot CLI |
| LLM scoring | Optional | Set `OPENAI_API_KEY` in `.env`, pass `--use-llm` | Keyword mode works without API key |

### Setup

```bash
# On Ubuntu/Debian Cloud VMs, if venv fails: sudo apt install python3.12-venv
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

VM update script: `pip install -r requirements.txt` (activate `.venv` first if you use one).

### Tests

```bash
source .venv/bin/activate
pytest agents/job-search/tests/ -q
```

### Notes

- Docker is not installed on the default Cloud Agent VM.
- Resume files live in `resume-output/` (do not commit secrets or API keys).
- Auto-apply is **not** implemented; future phases require human-in-the-loop.

## Repository layout

See root `README.md` and `docs/GETTING_STARTED.md`.

Priority agent: `agents/job-search/` (LangGraph).
