# AGENTS.md

Guidance for AI agents working in this repository.

## Repository status

This is a **greenfield repository**. As of the initial commit, the only tracked file is `README.md` (title: "AI-Agents-Research"). There is no application source, dependency manifest, test suite, linter config, or service definitions yet.

## Cursor Cloud specific instructions

### Services

| Service | Status | Notes |
|---------|--------|-------|
| Application server | Not present | No backend or frontend code exists yet. |
| Database | Not present | No database configuration. |
| Docker Compose | Not present | Docker is not installed on the default Cloud Agent VM. |

There is nothing to start, lint, test, or build until project scaffolding is added.

### VM tooling (available now)

The Cloud Agent VM includes:

- **Git** 2.43+
- **Node.js** v22.x with **npm** 10.x
- **Python** 3.12 with **pip**

When you add code, choose the stack that fits the project and add the corresponding dependency files (`package.json`, `pyproject.toml`, `requirements.txt`, etc.) plus run instructions to this file.

### Recommended next steps (when implementing)

1. Add a dependency manifest and lockfile for the chosen stack.
2. Add a `README.md` section with install, run, test, and lint commands.
3. Add `.env.example` if the project needs API keys (likely for AI/LLM providers).
4. Update this file with concrete service names, ports, and startup commands.

### Update script behavior

The VM update script is a no-op (`true`) because there are no dependencies to refresh. Replace it via **SetupVmEnvironment** once dependency manifests are added (for example: `npm install`, `pip install -r requirements.txt`, or `uv sync`).
