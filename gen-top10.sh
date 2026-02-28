#!/bin/bash
echo '{'
echo '  "generated": "'$(date -u +"%Y-%m-%d %H:%M")'",'
echo '  "total_ideas": '$(wc -l < brand-ideas.jsonl)','
echo '  "total_candidates_evaluated": '$(wc -l < candidates.jsonl)','
echo '  "total_rejected": '$(wc -l < rejected.jsonl)','
echo '  "top10": '
cat brand-ideas.jsonl | jq -s 'sort_by(-.score_avg) | .[0:10]'
echo '}'
