# International Product Discovery

Automated product scout finding overseas consumer products with no good US equivalent.

## Files

- `discoveries.jsonl` — Validated products that passed all checks
- `candidates.jsonl` — Raw candidates before validation
- `rejected.jsonl` — Products that failed validation (with reasons)
- `regions-tracker.json` — Coverage tracking per region/category
- `top10.json` — Auto-generated top 10 by score
- `run-log.jsonl` — Run history and stats

## Workflow

Runs every 20 minutes via OpenClaw cron. Each run:
1. Picks underexplored region + rotates category
2. Generates 15-25 candidates via web search
3. Validates top 3-5 deeply (Amazon check, US alternative check, demand signals)
4. Scores on 6 dimensions (demand, gap, importability, margin, defensibility, wow)
5. Updates tracker and regenerates top10
6. Git commits results

Goal: 1000+ candidates → 100+ discoveries → top 10 winners
