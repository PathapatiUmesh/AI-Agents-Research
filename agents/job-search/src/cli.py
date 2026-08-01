from __future__ import annotations

import argparse
from pathlib import Path

from dotenv import load_dotenv

from .graph import run_agent


def format_report(matches) -> str:
    lines = ["=" * 72, "JOB MATCH REPORT", "=" * 72, ""]
    for i, match in enumerate(matches, start=1):
        job = match.job
        lines.append(f"{i}. [{match.score}/100] {job.title} @ {job.company}")
        lines.append(f"   Location: {job.location}")
        lines.append(f"   URL: {job.url}")
        for reason in match.reasons:
            lines.append(f"   + {reason}")
        if match.missing_skills:
            lines.append(f"   - Gaps: {', '.join(match.missing_skills[:5])}")
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    load_dotenv()
    parser = argparse.ArgumentParser(description="Job search agent — resume match MVP")
    parser.add_argument(
        "--resume",
        type=Path,
        default=Path("resume-output/Umesh_Chandra_PV_ATS_Resume_DevOps_SRE_AI.txt"),
        help="Path to resume text file",
    )
    parser.add_argument("--use-llm", action="store_true", help="Use OpenAI for scoring (requires OPENAI_API_KEY)")
    parser.add_argument("--top", type=int, default=10, help="Show top N matches")
    args = parser.parse_args()

    if not args.resume.exists():
        raise SystemExit(f"Resume not found: {args.resume}")

    state = run_agent(str(args.resume), use_llm=args.use_llm)
    print(format_report(state.matches[: args.top]))
    print(f"Scored {len(state.matches)} jobs using {'LLM' if args.use_llm else 'keyword'} mode.")


if __name__ == "__main__":
    main()
