#!/usr/bin/env python3
import json
import sys
from pathlib import Path

# Load all ideas
ideas = []
with open(Path.home() / '.openclaw/workspace/nova/international-products-research/brand-ideas.jsonl', 'r') as f:
    for idx, line in enumerate(f, 1):
        if line.strip():
            try:
                ideas.append(json.loads(line))
            except json.JSONDecodeError as e:
                print(f"Error on line {idx}: {e}", file=sys.stderr)

# Filter to only valid dict objects
ideas_valid = [idea for idea in ideas if isinstance(idea, dict)]
print(f"Valid ideas: {len(ideas_valid)} of {len(ideas)}", flush=True)

# Sort by score_avg DESC
ideas_sorted = sorted(ideas_valid, key=lambda x: x.get('score_avg', 0), reverse=True)

# Batch 2: ideas 11-20 (index 10-19)
batch2_ideas = ideas_sorted[10:20]

print(f"Total ideas loaded: {len(ideas)}", flush=True)
print(f"Batch 2 (ideas 11-20) IDs and scores:", flush=True)
if len(ideas_sorted) >= 20:
    for i, idea in enumerate(batch2_ideas, start=11):
        print(f"{i}. {idea['id']}: {idea.get('us_brand_concept', 'NO CONCEPT')[:50]}... | score_avg: {idea.get('score_avg', 'N/A')}", flush=True)
else:
    print(f"ERROR: Only {len(ideas_sorted)} valid ideas found. Need at least 20.", flush=True)
