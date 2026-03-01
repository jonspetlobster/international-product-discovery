#!/usr/bin/env python3
"""
Update batch 2 ideas with competitive validation and revised scores
"""
import json
from pathlib import Path

# Revised scores for batch 2 ideas
batch2_updates = {
    "idea_236": {  # ClearHead
        "competitive_validation": "NAZ and SniffElixir already position nasal inhalers as focus/productivity tools. Market has multiple brands selling menthol inhalers for alertness. The 'twist' (productivity vs medicinal) already exists.",
        "scores": {"demand_proof": 4, "us_gap": 3, "manufacturing_ease": 9, "twist_strength": 4, "margin_potential": 7, "brandability": 8, "low_capital_start": 9},
        "score_avg": 4.5
    },
    "idea_525": {  # PICANTE
        "competitive_validation": "Tajín already sells chamoy products (sauce + seasoning). Competing against dominant Tajín brand with massive distribution. Format differentiation (premium shaker) is marginal.",
        "scores": {"demand_proof": 8, "us_gap": 6, "manufacturing_ease": 10, "twist_strength": 5, "margin_potential": 6, "brandability": 7, "low_capital_start": 9},
        "score_avg": 5.2
    },
    "idea_526": {  # FUEGO JUICE
        "competitive_validation": "Pickle Brine brand ALREADY sells jalapeño-spiced pickle juice as cocktail mixer/drink. PickleSplash exists. US gap claim of 10/10 is false - product literally exists with same positioning.",
        "scores": {"demand_proof": 4, "us_gap": 2, "manufacturing_ease": 10, "twist_strength": 3, "margin_potential": 7, "brandability": 6, "low_capital_start": 10},
        "score_avg": 4.0
    },
    "idea_312": {  # PandanCo
        "competitive_validation": "Pandan fragrance oils exist (DIY only). Dewy Monday sells pandan body oil. True gap for major brand, but pandan is unknown to 99% of Americans. Massive education barrier. Demand highly speculative.",
        "scores": {"demand_proof": 3, "us_gap": 9, "manufacturing_ease": 9, "twist_strength": 8, "margin_potential": 8, "brandability": 10, "low_capital_start": 7},
        "score_avg": 5.8
    },
    "idea_323": {  # QuickStick
        "competitive_validation": "No instant sticky rice products found (true gap). But Thai grocers sell pre-cooked versions. Niche within niche - sticky rice users are small % of rice consumers. Home demand for mango sticky rice unproven.",
        "scores": {"demand_proof": 6, "us_gap": 10, "manufacturing_ease": 7, "twist_strength": 8, "margin_potential": 7, "brandability": 7, "low_capital_start": 8},
        "score_avg": 5.5
    },
    "idea_332": {  # Ritual Mate
        "competitive_validation": "Amazon has dozens of mate gourd sets ($20-40). BALIBETOV, thebmate exist. Premium gap exists but mate adoption slow in US. Taste polarizing, high abandonment rate. Better than most batch 2 ideas.",
        "scores": {"demand_proof": 6, "us_gap": 7, "manufacturing_ease": 9, "twist_strength": 8, "margin_potential": 8, "brandability": 10, "low_capital_start": 8},
        "score_avg": 6.5
    },
    "idea_398": {  # SCRAPE PERFORMANCE
        "competitive_validation": "FeelFree Sport, STICKON, Allshow, GYX COELE all sell stainless steel gua sha/IASTM tools for athletic recovery. Amazon has 100+ products. US gap claim of 10/10 is false - market is flooded.",
        "scores": {"demand_proof": 7, "us_gap": 2, "manufacturing_ease": 10, "twist_strength": 3, "margin_potential": 5, "brandability": 6, "low_capital_start": 9},
        "score_avg": 4.2
    },
    "idea_626": {  # NightDrop
        "competitive_validation": "~10 liquid sleep tinctures on Amazon (gap confirmed). Premium glass dropper differentiator. But melatonin gummies dominate. Alcohol-based tinctures have shipping/regulatory challenges. Ritual positioning unproven.",
        "scores": {"demand_proof": 7, "us_gap": 9, "manufacturing_ease": 7, "twist_strength": 7, "margin_potential": 8, "brandability": 10, "low_capital_start": 8},
        "score_avg": 6.0
    },
    "idea_634": {  # Kasbah
        "competitive_validation": "No cumin finishing salt brands found (true gap). Finishing salt market strong. But cumin is polarizing flavor, easy to DIY, low barrier to entry. Sampling crucial. Best of batch 2.",
        "scores": {"demand_proof": 5, "us_gap": 10, "manufacturing_ease": 10, "twist_strength": 7, "margin_potential": 9, "brandability": 9, "low_capital_start": 10},
        "score_avg": 6.8
    },
    "idea_701": {  # HerBalance
        "competitive_validation": "Honeybush exists (Numi, Republic of Tea) but generic. No honeybush menopause brand (gap confirmed). But black cohosh dominates menopause tea. Education barrier on honeybush. FDA claims restrictions strict.",
        "scores": {"demand_proof": 7, "us_gap": 7, "manufacturing_ease": 9, "twist_strength": 7, "margin_potential": 9, "brandability": 8, "low_capital_start": 8},
        "score_avg": 6.2
    }
}

# Load ideas
input_path = Path.home() / '.openclaw/workspace/nova/international-products-research/brand-ideas.jsonl'
output_path = Path.home() / '.openclaw/workspace/nova/international-products-research/brand-ideas-updated.jsonl'

ideas = []
with open(input_path, 'r') as f:
    for line in f:
        if line.strip():
            try:
                idea = json.loads(line)
                if isinstance(idea, dict):
                    ideas.append(idea)
            except:
                pass

print(f"Loaded {len(ideas)} valid ideas")

# Update batch 2 ideas
updated_count = 0
for idea in ideas:
    idea_id = idea.get('id')
    if idea_id in batch2_updates:
        update_data = batch2_updates[idea_id]
        idea['competitive_validation'] = update_data['competitive_validation']
        idea['scores'] = update_data['scores']
        idea['score_avg'] = update_data['score_avg']
        updated_count += 1
        print(f"Updated {idea_id}: {idea['us_brand_concept'][:50]}... | score_avg: {idea['score_avg']}")

# Write updated JSONL
with open(output_path, 'w') as f:
    for idea in ideas:
        f.write(json.dumps(idea) + '\n')

print(f"\nUpdated {updated_count} ideas")
print(f"Written to: {output_path}")
print("Review the file, then replace brand-ideas.jsonl")
