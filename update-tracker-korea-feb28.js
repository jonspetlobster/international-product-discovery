const fs = require('fs');
const tracker = JSON.parse(fs.readFileSync('regions-tracker.json', 'utf8'));

// Update south_korea
tracker.regions.south_korea.candidates += 20;
tracker.regions.south_korea.ideas += 4;

// Update categories_recent (add grocery-pantry, keep last 5)
tracker.categories_recent.push('grocery-pantry');
if (tracker.categories_recent.length > 5) {
  tracker.categories_recent.shift();
}

// Update totals
tracker.total_candidates += 20;
tracker.total_ideas += 4;

fs.writeFileSync('regions-tracker.json', JSON.stringify(tracker, null, 2));
console.log('Updated tracker: south_korea +20 candidates, +4 ideas');
