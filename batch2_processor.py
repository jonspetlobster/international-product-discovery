#!/usr/bin/env python3
"""
Batch 2 competitive revalidation processor
Extracts ideas 11-20 from brand-ideas.jsonl for validation
"""
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
                pass  # Skip corrupted lines

# Filter to valid dicts
ideas_valid = [idea for idea in ideas if isinstance(idea, dict)]

# Sort by score_avg DESC
ideas_sorted = sorted(ideas_valid, key=lambda x: x.get('score_avg', 0), reverse=True)

# Batch 2: ideas 11-20 (index 10-19)
batch2_ideas = ideas_sorted[10:20]

# Export for validation
output_path = Path.home() / '.openclaw/workspace/nova/international-products-research/batch2_to_validate.jsonl'
with open(output_path, 'w') as f:
    for idea in batch2_ideas:
        f.write(json.dumps(idea) + '\n')

print(f"Extracted {len(batch2_ideas)} ideas for Batch 2 validation")
print(f"Written to: {output_path}")
for i, idea in enumerate(batch2_ideas, start=11):
    print(f"{i}. {idea['id']}: {idea['us_brand_concept'][:60]}...")
