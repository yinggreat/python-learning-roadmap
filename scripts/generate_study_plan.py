from __future__ import annotations

import argparse
import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
ROADMAP_FILE = REPO_ROOT / "data" / "roadmap.json"
PROFILE_FILE = REPO_ROOT / "data" / "study_profiles.json"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def load_phase_map() -> dict[str, dict]:
    roadmap = load_json(ROADMAP_FILE)
    return {phase["slug"]: phase for phase in roadmap["phases"]}


def load_track(track_slug: str) -> dict:
    profiles = load_json(PROFILE_FILE)
    for track in profiles["tracks"]:
        if track["slug"] == track_slug:
            return track
    available = ", ".join(track["slug"] for track in profiles["tracks"])
    raise SystemExit(f"Unknown track '{track_slug}'. Available tracks: {available}")


def build_weeks(track: dict, phase_map: dict[str, dict], weeks: int, focus: str | None, weekly_hours: int) -> list[dict]:
    order = list(track["recommended_order"])
    if focus and focus in order:
        order.remove(focus)
        order.insert(1, focus)

    weeks_per_phase = max(2, weeks // len(order))
    plan: list[dict] = []
    current_week = 1

    for slug in order:
        phase = phase_map[slug]
        for _ in range(weeks_per_phase):
            if current_week > weeks:
                break
            keyword_index = (current_week - 1) % len(phase["keywords"])
            project_index = (current_week - 1) % len(phase["projects"])
            plan.append(
                {
                    "week": current_week,
                    "phase": phase["title"],
                    "objective": phase["goal"],
                    "focus_keyword": phase["keywords"][keyword_index],
                    "project": phase["projects"][project_index],
                    "hours": weekly_hours,
                }
            )
            current_week += 1

    while current_week <= weeks:
        phase = phase_map[order[-1]]
        plan.append(
            {
                "week": current_week,
                "phase": phase["title"],
                "objective": "Consolidate earlier work, polish one portfolio project, and prepare a summary post.",
                "focus_keyword": "portfolio polish",
                "project": phase["projects"][0],
                "hours": weekly_hours,
            }
        )
        current_week += 1

    return plan


def render_markdown(track: dict, plan: list[dict], focus: str | None, weekly_hours: int) -> str:
    lines = [
        f"# {track['title']} - Python 12 周学习计划",
        "",
        f"- 学习画像：{track['description']}",
        f"- 每周投入：{weekly_hours} 小时",
        f"- 特别关注：{focus or '按默认成长顺序推进'}",
        f"- 强调能力：{' / '.join(track['emphasis'])}",
        "",
        "## Weekly Plan",
    ]

    for item in plan:
        lines.extend(
            [
                f"### Week {item['week']} | {item['phase']}",
                f"- 本周目标：{item['objective']}",
                f"- 重点关键词：{item['focus_keyword']}",
                f"- 建议项目：{item['project']}",
                f"- 建议投入：{item['hours']} 小时",
                "",
            ]
        )

    lines.extend(
        [
            "## 建议执行方式",
            "- 每周至少保留 1 次复盘，把遇到的报错和解决办法记录下来。",
            "- 每 2 周输出一个小项目，而不是只记语法笔记。",
            "- 第 12 周把最好的项目整理成 GitHub 作品集入口。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a personalized Python study plan.")
    parser.add_argument("--track", default="career-switcher", help="Track slug, such as beginner or career-switcher")
    parser.add_argument("--focus", help="Optional focus phase slug, such as automation or data-analysis")
    parser.add_argument("--weeks", type=int, default=12, help="Number of study weeks")
    parser.add_argument("--weekly-hours", type=int, default=10, help="Study hours per week")
    parser.add_argument("--output", help="Optional path to save the Markdown plan")
    args = parser.parse_args()

    phase_map = load_phase_map()
    track = load_track(args.track)
    plan = build_weeks(track, phase_map, args.weeks, args.focus, args.weekly_hours)
    markdown = render_markdown(track, plan, args.focus, args.weekly_hours)

    if args.output:
        output_path = Path(args.output)
        output_path.write_text(markdown, encoding="utf-8")
        print(f"Study plan written to {output_path.resolve()}")
        return

    print(markdown)


if __name__ == "__main__":
    main()
