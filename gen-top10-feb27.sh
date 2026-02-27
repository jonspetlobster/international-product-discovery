#!/bin/bash
# Read all brand ideas, sort by score_avg, take top 10

# Use jq if available, otherwise python
if command -v jq &> /dev/null; then
    echo '{"generated":"'$(date -u +%Y-%m-%dT%H:%M:%S)'","total_ideas":'$(wc -l < brand-ideas.jsonl)',"total_candidates_evaluated":'$(wc -l < candidates.jsonl)',"total_rejected":'$(wc -l < rejected.jsonl)',"top10":[' > top10.json
    cat brand-ideas.jsonl | jq -s 'sort_by(-.score_avg) | .[0:10]' | tail -n +2 | head -n -1 >> top10.json
    echo ']}' >> top10.json
else
    # Python fallback
    python3 << 'PYTHON'
import json
from datetime import datetime

ideas = []
with open('brand-ideas.jsonl', 'r') as f:
    for line in f:
        ideas.append(json.loads(line))

ideas_sorted = sorted(ideas, key=lambda x: x.get('score_avg', 0), reverse=True)
top10 = ideas_sorted[:10]

with open('rejected.jsonl', 'r') as f:
    total_rejected = sum(1 for _ in f)

with open('candidates.jsonl', 'r') as f:
    total_candidates = sum(1 for _ in f)

result = {
    "generated": datetime.utcnow().strftime('%Y-%m-%d %H:%M'),
    "total_ideas": len(ideas),
    "total_candidates_evaluated": total_candidates,
    "total_rejected": total_rejected,
    "top10": top10
}

with open('top10.json', 'w') as f:
    json.dump(result, f, indent=2)
    
print(f"Generated top10.json with {len(top10)} ideas")
PYTHON
fi
