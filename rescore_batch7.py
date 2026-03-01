#!/usr/bin/env python3
import json

# Read all ideas
ideas = []
with open('brand-ideas.jsonl', 'r') as f:
    for line in f:
        ideas.append(json.loads(line))

# IDs to update with validation results
updates = {
    "idea_238": {  # Laundry Lab Kit
        "competitive_validation": {
            "date": "2026-03-01",
            "verdict": "REJECT - Direct competitor exists",
            "findings": "Lehman's Homemade Laundry Soap Starter Set (sold at Walmart/Lehmans.com) offers complete DIY laundry kit with ingredients, jars, and recipes for 800 loads. Established brand serving exact target market.",
            "competitors": ["Lehman's Homemade Laundry Soap Starter Set"],
            "gap_assessment": "No gap - complete kit already exists with strong brand presence"
        },
        "scores": {"demand_proof": 7, "us_gap": 2, "manufacturing_ease": 10, "twist_strength": 3, "margin_potential": 5, "brandability": 6, "low_capital_start": 10},
        "score_avg": 6.14
    },
    "idea_251": {  # BeanGlow
        "competitive_validation": {
            "date": "2026-03-01",
            "verdict": "REJECT - Format already exists",
            "findings": "FANCL Deep Clear Enzyme Powder comes in single-use capsules (30-pack). Suisai is another major Japanese enzyme powder cleanser. Booni Doon offers cleansing capsules. The single-use pod format is NOT unique.",
            "competitors": ["FANCL Deep Clear Enzyme Powder (capsules)", "Suisai enzyme powder", "Booni Doon cleansing capsules"],
            "gap_assessment": "No gap - single-use enzyme powder format well-established"
        },
        "scores": {"demand_proof": 7, "us_gap": 2, "manufacturing_ease": 7, "twist_strength": 3, "margin_potential": 8, "brandability": 7, "low_capital_start": 7},
        "score_avg": 5.86
    },
    "idea_267": {  # ForageKit
        "competitive_validation": {
            "date": "2026-03-01",
            "verdict": "REJECT - Complete kit already exists",
            "findings": "Seajan 18-Pc Mushroom Foraging Kit on Amazon includes knife, brush, 15 guide cards, and field notebook. Foxyoo also sells complete foraging kits. The bundled kit concept with ID cards is already executed.",
            "competitors": ["Seajan 18-Pc Mushroom Foraging Kit", "Foxyoo Mushroom Foraging Kit"],
            "gap_assessment": "No gap - complete foraging kits with educational materials widely available"
        },
        "scores": {"demand_proof": 8, "us_gap": 2, "manufacturing_ease": 8, "twist_strength": 3, "margin_potential": 6, "brandability": 7, "low_capital_start": 7},
        "score_avg": 5.86
    },
    "idea_287": {  # HawGood
        "competitive_validation": {
            "date": "2026-03-01",
            "verdict": "REJECT - Product format exists",
            "findings": "Haw flakes (hawthorn candy) widely available on Amazon from multiple brands: BESTORE, Phuumy, etc. While positioned as Chinese snacks (not premium wellness), the product itself exists and is accessible. Premium repositioning alone is weak differentiator.",
            "competitors": ["BESTORE Haw Flakes", "Phuumy Hawthorn Bar", "Generic haw flakes"],
            "gap_assessment": "Partial gap in premium wellness positioning, but product format saturated"
        },
        "scores": {"demand_proof": 7, "us_gap": 3, "manufacturing_ease": 7, "twist_strength": 4, "margin_potential": 6, "brandability": 6, "low_capital_start": 6},
        "score_avg": 5.57
    },
    "idea_296": {  # ChillMist
        "competitive_validation": {
            "date": "2026-03-01",
            "verdict": "REJECT - Cooling spray exists",
            "findings": "'Pet Your Pet Refresh Cooling Spray for Dogs' exists on Walmart. NaturVet Quiet Moments makes calming aromatherapy sprays for dogs. The cooling + aromatherapy combo may be unique but both categories are served.",
            "competitors": ["Pet Your Pet Refresh Cooling Spray", "NaturVet Quiet Moments Calming Spray"],
            "gap_assessment": "No significant gap - cooling and calming sprays both exist"
        },
        "scores": {"demand_proof": 6, "us_gap": 3, "manufacturing_ease": 9, "twist_strength": 4, "margin_potential": 7, "brandability": 7, "low_capital_start": 8},
        "score_avg": 6.29
    },
    "idea_300": {  # VitalShot
        "competitive_validation": {
            "date": "2026-03-01",
            "verdict": "REJECT - Wellness shot glass kits exist",
            "findings": "Multiple Amazon sellers offer 2oz wellness shot glass bottle kits with recipe booklets, labels, and markers: Juice Shot Bottles Kit, AuroTrends Ginger Shots Bottles, zsccxq wellness shot bottles. Complete kits already available.",
            "competitors": ["Juice Shot Bottles Kit (16-pack with recipe booklet)", "AuroTrends 2oz Ginger Shots Bottles", "zsccxq Wellness Shot Bottles"],
            "gap_assessment": "No gap - wellness shot glass kits with recipes widely available"
        },
        "scores": {"demand_proof": 7, "us_gap": 2, "manufacturing_ease": 9, "twist_strength": 3, "margin_potential": 7, "brandability": 6, "low_capital_start": 8},
        "score_avg": 6.0
    },
    "idea_305": {  # LineSmooth
        "competitive_validation": {
            "date": "2026-03-01",
            "verdict": "REJECT - Exact positioning exists",
            "findings": "NYX Smushy Matte Lip Balm specifically advertises 'blurred color that blurs the appearance of lip lines' with a matte finish. This is the EXACT positioning (matte finish to hide lines on mature lips). No gap.",
            "competitors": ["NYX Smushy Matte Lip Balm"],
            "gap_assessment": "No gap - exact product positioning already exists from established brand"
        },
        "scores": {"demand_proof": 6, "us_gap": 1, "manufacturing_ease": 9, "twist_strength": 2, "margin_potential": 7, "brandability": 6, "low_capital_start": 8},
        "score_avg": 5.57
    },
    "idea_329": {  # PiePress
        "competitive_validation": {
            "date": "2026-03-01",
            "verdict": "REJECT - Tool widely available",
            "findings": "Stainless steel empanada crimpers/presses widely available on Amazon from KAYCROWN, Proshopping, COTEY, etc. Multiple sizes (4\", 5\", 6\"). While premium branding + recipe book could add value, the core tool is saturated.",
            "competitors": ["KAYCROWN Empanada Press (stainless)", "Proshopping Empanada Press", "COTEY Dumpling Maker", "Goya-branded presses"],
            "gap_assessment": "No significant gap - tool available in multiple sizes/brands, premium branding alone is weak differentiator"
        },
        "scores": {"demand_proof": 7, "us_gap": 2, "manufacturing_ease": 9, "twist_strength": 3, "margin_potential": 7, "brandability": 6, "low_capital_start": 8},
        "score_avg": 6.0
    },
    "idea_337": {  # GrowthShot - POSSIBLE GAP
        "competitive_validation": {
            "date": "2026-03-01",
            "verdict": "VIABLE - Unique format gap identified",
            "findings": "All castor oil hair growth products are bottled (Jamaican Black Castor Oil, Sky Organics, etc.). No single-use sachets/pods found. Format innovation is genuine. However, efficacy claims need validation and men's hair loss market is competitive (Rogaine, finasteride).",
            "competitors": ["Bottled castor oil brands (no sachet format)"],
            "gap_assessment": "Format gap exists - single-use castor oil sachets not found. Moderate opportunity but requires strong execution."
        },
        "scores": {"demand_proof": 7, "us_gap": 7, "manufacturing_ease": 6, "twist_strength": 7, "margin_potential": 7, "brandability": 7, "low_capital_start": 7},
        "score_avg": 6.86
    },
    "idea_342": {  # Cape Table
        "competitive_validation": {
            "date": "2026-03-01",
            "verdict": "REJECT - Category exists",
            "findings": "Saucy Susan makes peach apricot sauce/glaze marketed for grilling. The Gracious Gourmet offers Peach Apricot Chutney. Terrapin Ridge Farms has Apricot Ginger Teriyaki Glaze. Fruit chutney for grilling/entertaining exists.",
            "competitors": ["Saucy Susan Peach Apricot Sauce", "The Gracious Gourmet Peach Apricot Chutney", "Terrapin Ridge Farms glazes"],
            "gap_assessment": "Partial gap in premium Mrs Balls-style branding, but category served by multiple brands"
        },
        "scores": {"demand_proof": 6, "us_gap": 3, "manufacturing_ease": 9, "twist_strength": 4, "margin_potential": 7, "brandability": 7, "low_capital_start": 7},
        "score_avg": 6.14
    }
}

# Update the ideas
for idea in ideas:
    if idea["id"] in updates:
        idea["competitive_validation"] = updates[idea["id"]]["competitive_validation"]
        idea["scores"] = updates[idea["id"]]["scores"]
        idea["score_avg"] = updates[idea["id"]]["score_avg"]

# Write back
with open('brand-ideas.jsonl', 'w') as f:
    for idea in ideas:
        f.write(json.dumps(idea) + '\n')

print("Updated 10 ideas with competitive validation and re-scored")
