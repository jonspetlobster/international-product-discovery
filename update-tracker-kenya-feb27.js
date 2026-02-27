const fs = require('fs');
const tracker = JSON.parse(fs.readFileSync('regions-tracker.json', 'utf8'));

tracker.regions.kenya.candidates += 20;
tracker.regions.kenya.ideas += 3;
tracker.total_candidates += 20;
tracker.total_ideas += 3;

// Update recent categories
tracker.categories_recent.push('cleaning');
if (tracker.categories_recent.length > 5) {
  tracker.categories_recent.shift();
}

fs.writeFileSync('regions-tracker.json', JSON.stringify(tracker, null, 2));
console.log('Tracker updated: Kenya +20 candidates, +3 ideas');
