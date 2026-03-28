from __future__ import annotations

import argparse
import json
from pathlib import Path


DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "roadmap.json"


def load_roadmap() -> dict:
    return json.loads(DATA_FILE.read_text(encoding="utf-8"))


def print_phase(phase: dict) -> None:
    print(f"[{phase['title']}]")
    print(f"Goal: {phase['goal']}")
    print("Keywords:")
    for keyword in phase["keywords"]:
        print(f"  - {keyword}")
    print("Suggested projects:")
    for project in phase["projects"]:
        print(f"  - {project}")
    print()


def main() -> None:
    parser = argparse.ArgumentParser(description="Show the Python learning roadmap.")
    parser.add_argument(
        "--phase",
        help="Optional phase slug, for example: foundations, automation, public-data-collection",
    )
    args = parser.parse_args()

    phases = load_roadmap()["phases"]

    if args.phase:
        matched = [phase for phase in phases if phase["slug"] == args.phase]
        if not matched:
            available = ", ".join(phase["slug"] for phase in phases)
            raise SystemExit(f"Unknown phase '{args.phase}'. Available phases: {available}")
        print_phase(matched[0])
        return

    for phase in phases:
        print_phase(phase)


if __name__ == "__main__":
    main()
