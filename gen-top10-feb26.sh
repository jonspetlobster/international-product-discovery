#!/bin/bash
total_ideas=$(wc -l < brand-ideas.jsonl)
total_candidates=$(wc -l < candidates.jsonl)
total_rejected=$(wc -l < rejected.jsonl)

cat brand-ideas.jsonl | jq -s "sort_by(-.score_avg) | {
  generated: \"$(date '+%Y-%m-%d %H:%M')\",
  total_ideas: $total_ideas,
  total_candidates_evaluated: $total_candidates,
  total_rejected: $total_rejected,
  top10: .[0:10]
}" > top10.json

echo "Generated top10.json with $total_ideas ideas, top 10 by score"
