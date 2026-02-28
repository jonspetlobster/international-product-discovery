const fs = require('fs');
const tracker = JSON.parse(fs.readFileSync('regions-tracker.json', 'utf8'));

tracker.regions.turkey.candidates += 12;
tracker.regions.turkey.ideas += 5;
tracker.total_candidates += 12;
tracker.total_ideas += 5;
tracker.total_rejected += 7;

// Update categories_recent (keep last 5)
tracker.categories_recent.unshift('health-wellness');
if (tracker.categories_recent.length > 5) {
  tracker.categories_recent = tracker.categories_recent.slice(0, 5);
}

fs.writeFileSync('regions-tracker.json', JSON.stringify(tracker, null, 2));
console.log('Updated tracker: turkey +12 candidates, +5 ideas, +7 rejected');
