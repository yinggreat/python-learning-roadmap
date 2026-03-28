# Contributing

Thanks for your interest in improving this teaching repository.

## What Contributions Are Welcome

- roadmap refinement suggestions
- typo or documentation fixes
- more realistic project recommendations for each stage
- new learner profiles for different goals

## Contribution Rules

- keep examples beginner-friendly and project-oriented
- prefer clear names and concise explanations over clever abstractions
- avoid content that encourages scraping abuse, policy violations, or unsafe automation
- update `CHANGELOG.md` when the change is user-visible

## Local Checks

Run these before opening a pull request:

```bash
python scripts/show_roadmap.py
python scripts/generate_study_plan.py --track career-switcher --focus automation --weeks 12
```
