#!/usr/bin/env python3
import json

# Revalidation data for batch 1 (ideas 1-10)
revalidations = {
    "idea_001": {
        "competitive_validation": "Amazon/Target: Good & Gather Umami Seasoning blend exists at Target. Yondu plant-based umami sauce dominates. Multiple mushroom/kelp umami products. Gap smaller than expected - lentil-based is unique but umami category is crowded. Protein angle differentiated.",
        "scores": {
            "demand_proof": 7,
            "us_gap": 5,  # reduced from 9
            "manufacturing_ease": 10,
            "twist_strength": 6,  # reduced from 9
            "margin_potential": 8,
            "brandability": 7,
            "low_capital_start": 10
        },
        "score_avg": 7.6
    },
    "idea_033": {
        "competitive_validation": "Amazon/Retail: Nora Mill Cinnamon Toast Sprinkles shaker jar exists. Red Ape Cinnamon Sugar Shake. Multiple cinnamon sugar shakers on Amazon/Walmart. NOT a unique format. Breakfast sprinkle concept exists, just not heavily marketed.",
        "scores": {
            "demand_proof": 4,  # reduced from 5
            "us_gap": 3,  # reduced from 10 - MAJOR
            "manufacturing_ease": 10,
            "twist_strength": 5,  # reduced from 9
            "margin_potential": 7,
            "brandability": 6,
            "low_capital_start": 10
        },
        "score_avg": 6.4
    },
    "idea_013": {
        "competitive_validation": "Luxury hand sanitizer market SATURATED post-COVID. Paume (cedar/orange/lemon), Diehl+Marcus (Citron), multiple DTC brands. FDA OTC drug regulations for hand sanitizer add complexity. Kolonya hospitality angle is unique but overall category is crowded and sanitizer fatigue is real.",
        "scores": {
            "demand_proof": 6,  # reduced from 8
            "us_gap": 4,  # reduced from 9 - MAJOR
            "manufacturing_ease": 7,  # reduced from 9 - FDA compliance
            "twist_strength": 7,
            "margin_potential": 7,
            "brandability": 9,
            "low_capital_start": 8
        },
        "score_avg": 6.9
    },
    "idea_002": {
        "competitive_validation": "No savory peanut seasoning found on Amazon/Target/Google Shopping. Everything Bagel Seasoning dominates savory sprinkle space but no peanut variant. True gap. However, peanut allergies severely limit addressable market. Shelf life concerns with ground peanuts (oil content).",
        "scores": {
            "demand_proof": 6,  # reduced from 7
            "us_gap": 8,  # kept high - true gap
            "manufacturing_ease": 9,
            "twist_strength": 7,
            "margin_potential": 7,
            "brandability": 8,
            "low_capital_start": 10
        },
        "score_avg": 7.9
    },
    "idea_037": {
        "competitive_validation": "Zero commercial US ghriba brands found. Only recipes exist online (MarocMama, SugarYums). Gluten-free almond cookie market has Mary's Gone Crackers, Simple Mills but no Moroccan offerings. Genuine gap. Tea-dunking positioning is novel.",
        "scores": {
            "demand_proof": 6,  # realistic
            "us_gap": 9,  # true gap
            "manufacturing_ease": 8,
            "twist_strength": 7,
            "margin_potential": 8,
            "brandability": 8,
            "low_capital_start": 9
        },
        "score_avg": 7.9
    },
    "idea_016": {
        "competitive_validation": "Traditional Medicinals dominates functional tea with multi-herb blends. Royal Herbs sells single sage tea but tiny presence. Single-herb pharma-grade positioning is differentiated BUT requires heavy consumer education vs. established brands. FDA health claim restrictions.",
        "scores": {
            "demand_proof": 6,
            "us_gap": 6,  # reduced from 9
            "manufacturing_ease": 9,
            "twist_strength": 6,  # reduced from 8
            "margin_potential": 7,
            "brandability": 8,
            "low_capital_start": 9
        },
        "score_avg": 7.3
    },
    "idea_010": {
        "competitive_validation": "Zero mainstream provenzal brands in US. Only low-quality imports (Saborigal) at Latin markets. Italian seasoning and herbes de Provence are different profiles. True white space for premium Argentine seasoning brand.",
        "scores": {
            "demand_proof": 5,  # realistic
            "us_gap": 9,  # true gap
            "manufacturing_ease": 10,
            "twist_strength": 7,
            "margin_potential": 8,
            "brandability": 8,
            "low_capital_start": 9
        },
        "score_avg": 8.0
    },
    "idea_034": {
        "competitive_validation": "KITSCH ALREADY SELLS 'Vanilla Dessert Hair Perfume' - exact same concept (gourmand scent, affordable, Gen Z, TikTok). Also has pistachio latte, amber shores. Direct competitor exists at $18-22 price point. Major overlap.",
        "scores": {
            "demand_proof": 7,
            "us_gap": 2,  # reduced from 9 - MAJOR FAIL
            "manufacturing_ease": 8,
            "twist_strength": 3,  # not unique
            "margin_potential": 6,
            "brandability": 7,
            "low_capital_start": 7
        },
        "score_avg": 5.7
    },
    "idea_022": {
        "competitive_validation": "Bottled nuoc mau EXISTS at Asian grocery stores but Viet World Kitchen confirms pre-made versions taste 'heinous' and 'very bitter.' Gap exists for quality version BUT recipe is trivial (sugar + water) - hard to justify premium. Niche market.",
        "scores": {
            "demand_proof": 7,
            "us_gap": 6,  # reduced from 10
            "manufacturing_ease": 9,
            "twist_strength": 5,  # reduced from 7
            "margin_potential": 7,
            "brandability": 7,
            "low_capital_start": 9
        },
        "score_avg": 7.1
    },
    "idea_032": {
        "competitive_validation": "Joppie sauce available in EU grocery stores and Dutch expat online shops. Multiple chimichurri dry blends exist: Gneiss Spice, The Spice Way, The Spice House, Savory Spice. Curry mayo fry sauce gap exists but competitive landscape is more crowded than claimed.",
        "scores": {
            "demand_proof": 5,
            "us_gap": 6,  # reduced from 9
            "manufacturing_ease": 9,
            "twist_strength": 6,  # reduced from 7
            "margin_potential": 8,
            "brandability": 7,
            "low_capital_start": 9
        },
        "score_avg": 7.1
    }
}

# Read original file
with open('brand-ideas.jsonl', 'r') as f:
    lines = f.readlines()

# Update first 10 ideas
updated_lines = []
for i, line in enumerate(lines):
    idea = json.loads(line)
    idea_id = idea['id']
    
    if idea_id in revalidations:
        # Add competitive validation and update scores
        idea['competitive_validation'] = revalidations[idea_id]['competitive_validation']
        idea['scores'] = revalidations[idea_id]['scores']
        idea['score_avg'] = revalidations[idea_id]['score_avg']
    
    updated_lines.append(json.dumps(idea) + '\n')

# Write updated file
with open('brand-ideas.jsonl', 'w') as f:
    f.writelines(updated_lines)

print("✅ Batch 1 revalidation complete. 10 ideas updated with competitive validation.")
print(f"📊 Score changes:")
for idea_id, data in revalidations.items():
    print(f"  {idea_id}: {data['score_avg']}/10")
