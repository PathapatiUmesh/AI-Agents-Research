import sys
from pathlib import Path

import pytest

AGENT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(AGENT_ROOT))

from src.job_fetcher import fetch_sample_jobs  # noqa: E402
from src.matcher import _score_keyword  # noqa: E402
from src.resume_loader import load_resume  # noqa: E402


@pytest.fixture
def resume_path():
    return (
        Path(__file__).resolve().parents[3]
        / "resume-output"
        / "Umesh_Chandra_PV_ATS_Resume_DevOps_SRE_AI.txt"
    )


def test_load_resume_extracts_skills(resume_path):
    state = load_resume(resume_path)
    assert "kubernetes" in state.skills
    assert "python" in state.skills
    assert len(state.target_roles) >= 1


def test_devops_job_scores_higher_than_frontend(resume_path):
    state = load_resume(resume_path)
    jobs = fetch_sample_jobs()
    devops = next(j for j in jobs if "DevOps" in j.title)
    frontend = next(j for j in jobs if "React" in j.title)
    devops_score = _score_keyword(devops, state).score
    frontend_score = _score_keyword(frontend, state).score
    assert devops_score > frontend_score


def test_sample_jobs_load():
    jobs = fetch_sample_jobs()
    assert len(jobs) >= 4
