const fs = require('fs');
const tracker = JSON.parse(fs.readFileSync('regions-tracker.json', 'utf8'));

// Update brazil: +20 candidates, +3 ideas
tracker.regions.brazil.candidates += 20;
tracker.regions.brazil.ideas += 3;

// Update categories_recent: add personal-care, remove oldest if >5
tracker.categories_recent.push('personal-care');
if (tracker.categories_recent.length > 5) {
  tracker.categories_recent.shift();
}

// Update totals
tracker.total_candidates += 20;
tracker.total_ideas += 3;

fs.writeFileSync('regions-tracker.json', JSON.stringify(tracker, null, 2));
console.log('Tracker updated: brazil +20 candidates, +3 ideas');
