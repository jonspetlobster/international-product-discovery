const fs = require('fs');
const tracker = JSON.parse(fs.readFileSync('regions-tracker.json', 'utf8'));

tracker.regions.vietnam.candidates += 23;
tracker.regions.vietnam.ideas += 5;
tracker.total_candidates += 23;
tracker.total_ideas += 5;
tracker.total_rejected += 18;

// Update categories_recent (keep last 5, add new, remove oldest)
tracker.categories_recent = tracker.categories_recent || [];
tracker.categories_recent.push('laundry-clothing');
if (tracker.categories_recent.length > 5) {
  tracker.categories_recent.shift();
}

fs.writeFileSync('regions-tracker.json', JSON.stringify(tracker, null, 2));
console.log('Updated tracker for Vietnam laundry run');
