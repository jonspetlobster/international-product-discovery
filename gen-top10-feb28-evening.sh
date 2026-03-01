#!/bin/bash
cd ~/.openclaw/workspace/nova/international-products-research

total_ideas=$(cat brand-ideas.jsonl | wc -l | tr -d ' ')
total_candidates=$(cat candidates.jsonl | wc -l | tr -d ' ')
total_rejected=$(cat rejected.jsonl | wc -l | tr -d ' ')

echo "{" > top10.json
echo "  \"generated\": \"2026-02-28 18:19\"," >> top10.json
echo "  \"total_ideas\": $total_ideas," >> top10.json
echo "  \"total_candidates_evaluated\": $total_candidates," >> top10.json
echo "  \"total_rejected\": $total_rejected," >> top10.json
echo "  \"top10\": " >> top10.json
cat brand-ideas.jsonl | jq -s 'sort_by(-.score_avg) | .[0:10]' >> top10.json
echo "}" >> top10.json

echo "Generated top10.json with $total_ideas total ideas"
