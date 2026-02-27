const fs = require('fs');
const tracker = JSON.parse(fs.readFileSync('regions-tracker.json', 'utf8'));

// Update Philippines
tracker.regions.philippines.candidates += 21;
tracker.regions.philippines.ideas += 4;

// Update categories_recent (keep last 5)
tracker.categories_recent.push('stationery');
if (tracker.categories_recent.length > 5) {
  tracker.categories_recent.shift();
}

// Update totals
tracker.total_candidates += 21;
tracker.total_ideas += 4;

fs.writeFileSync('regions-tracker.json', JSON.stringify(tracker, null, 2));
console.log('Updated tracker: Philippines +21 candidates, +4 ideas');
