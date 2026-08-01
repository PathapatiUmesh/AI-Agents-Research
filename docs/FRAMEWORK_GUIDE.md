# Framework Guide — When to Use What

## Decision tree

```
Is it a multi-step workflow with state and approvals?
  YES → LangGraph
  NO → Is it a team of roles collaborating on one deliverable?
          YES → CrewAI
          NO → Does it need to write/run code in a loop?
                  YES → AutoGen (or LangGraph + code tool)
                  NO → LangChain chain or simple script
```

## LangGraph — job-search, customer-ops routing

- **Strengths:** Graph state, persistence, interrupts (pause for human), production patterns
- **Learn:** [LangGraph quickstart](https://langchain-ai.github.io/langgraph/)
- **This repo:** `agents/job-search/src/graph.py`

## CrewAI — research reports, market monitoring

- **Strengths:** Intuitive roles (Researcher, Analyst, Editor)
- **Weakness:** Less fine-grained control than LangGraph for compliance-heavy flows
- **This repo:** Planned under `agents/research-data/`

## AutoGen — bug-fix, unit-tests, refactoring

- **Strengths:** Multi-agent coding conversations, execution
- **Caution:** Always sandbox code execution; never run unreviewed agent code on prod
- **This repo:** Planned under `agents/software-engineering/`

## Auto-apply ethics and ToS

Many job boards **prohibit** fully automated applications. Recommended pattern:

1. Agent **finds** and **scores** jobs
2. Agent **drafts** resume tweaks + cover letter
3. **You approve** each application
4. Optional: semi-automated form fill with Playwright where allowed

Never store passwords in repo; use `.env` and a secrets manager for production.
