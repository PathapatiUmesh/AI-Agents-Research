from __future__ import annotations

import json
from pathlib import Path

from .models import JobPosting


def fetch_sample_jobs(data_path: Path | None = None) -> list[JobPosting]:
    path = data_path or Path(__file__).resolve().parent.parent / "data" / "sample_jobs.json"
    raw = json.loads(path.read_text(encoding="utf-8"))
    return [JobPosting.model_validate(item) for item in raw]


def fetch_jobs(source: str = "sample", data_path: Path | None = None) -> list[JobPosting]:
    if source == "sample":
        return fetch_sample_jobs(data_path)
    raise ValueError(f"Unsupported job source: {source}. Use 'sample' until live APIs are wired.")
