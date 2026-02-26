const fs = require('fs');
const tracker = JSON.parse(fs.readFileSync('regions-tracker.json', 'utf8'));

// UK is index 11 based on default order
tracker.regions[11].candidates += 20;
tracker.regions[11].ideas += 3;

// Update categories_recent (keep last 5)
tracker.categories_recent = tracker.categories_recent || [];
tracker.categories_recent.push('fitness');
if (tracker.categories_recent.length > 5) {
  tracker.categories_recent.shift();
}

tracker.total_candidates += 20;
tracker.total_ideas += 3;

fs.writeFileSync('regions-tracker.json', JSON.stringify(tracker, null, 2));
console.log('Tracker updated: UK +20 candidates, +3 ideas');
