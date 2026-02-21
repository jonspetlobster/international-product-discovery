const fs = require('fs');
const tracker = JSON.parse(fs.readFileSync('regions-tracker.json', 'utf8'));

// Update Indonesia stats
tracker.regions.indonesia.candidates += 18;
tracker.regions.indonesia.ideas += 5;

// Update categories_recent (keep last 5, add snacks-candy, remove oldest)
tracker.categories_recent = tracker.categories_recent.slice(-4);
tracker.categories_recent.push('snacks-candy');

// Update totals
tracker.total_candidates += 18;
tracker.total_ideas += 5;

fs.writeFileSync('regions-tracker.json', JSON.stringify(tracker, null, 2));
console.log('✓ Updated tracker: Indonesia +18 candidates, +5 ideas');
