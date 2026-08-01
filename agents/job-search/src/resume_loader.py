from __future__ import annotations

import re
from pathlib import Path

from .models import AgentState

# Keywords aligned to Umesh's resume / target roles
DEFAULT_TARGET_ROLES = [
    "devops engineer",
    "site reliability engineer",
    "sre",
    "ai platform engineer",
    "platform engineer",
    "cloud engineer",
    "infrastructure engineer",
]

SKILL_PATTERNS = [
    "kubernetes",
    "helm",
    "docker",
    "ansible",
    "aws",
    "azure",
    "gcp",
    "grafana",
    "splunk",
    "python",
    "fastapi",
    "ci/cd",
    "terraform",
    "slo",
    "observability",
    "pyspark",
    "linux",
    "servicenow",
]


def load_resume(path: str | Path) -> AgentState:
    text = Path(path).read_text(encoding="utf-8")
    skills = _extract_skills(text)
    roles = _extract_target_roles(text)
    return AgentState(
        resume_path=str(path),
        resume_text=text,
        target_roles=roles or DEFAULT_TARGET_ROLES,
        skills=skills,
    )


def _extract_skills(text: str) -> list[str]:
    lowered = text.lower()
    found = [skill for skill in SKILL_PATTERNS if skill in lowered]
    return sorted(set(found))


def _extract_target_roles(text: str) -> list[str]:
    roles: list[str] = []
    for line in text.splitlines():
        if "target roles:" in line.lower():
            chunk = line.split(":", 1)[-1]
            roles.extend([r.strip().lower() for r in chunk.split(",") if r.strip()])
    if not roles:
        match = re.search(r"open to (.+?) roles", text, re.IGNORECASE)
        if match:
            roles = [r.strip().lower() for r in match.group(1).split(",")]
    return roles
