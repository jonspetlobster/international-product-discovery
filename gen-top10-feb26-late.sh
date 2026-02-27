#!/bin/bash
TOTAL_IDEAS=$(wc -l < brand-ideas.jsonl)
TOTAL_CANDIDATES=$(wc -l < candidates.jsonl)
TOTAL_REJECTED=$(wc -l < rejected.jsonl)
NOW=$(date -u +"%Y-%m-%d %H:%M")

echo "{" > top10.json
echo "  \"generated\": \"$NOW\"," >> top10.json
echo "  \"total_ideas\": $TOTAL_IDEAS," >> top10.json
echo "  \"total_candidates_evaluated\": $TOTAL_CANDIDATES," >> top10.json
echo "  \"total_rejected\": $TOTAL_REJECTED," >> top10.json
echo "  \"top10\": " >> top10.json
cat brand-ideas.jsonl | jq -s 'sort_by(-.score_avg) | .[0:10]' >> top10.json
echo "}" >> top10.json
