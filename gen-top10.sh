#!/bin/bash
IDEAS=$(cat brand-ideas.jsonl | wc -l | tr -d ' ')
CANDS=$(cat candidates.jsonl | wc -l | tr -d ' ')
REJ=$(cat rejected.jsonl | wc -l | tr -d ' ')
NOW=$(date -u +"%Y-%m-%d %H:%M")

cat > top10.json << ENDJSON
{
  "generated": "$NOW",
  "total_ideas": $IDEAS,
  "total_candidates_evaluated": $CANDS,
  "total_rejected": $REJ,
  "top10": $(cat top10-entries.json)
}
ENDJSON

rm top10-entries.json
echo "Top10 regenerated"
