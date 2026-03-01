const fs = require('fs');
const tracker = JSON.parse(fs.readFileSync('regions-tracker.json', 'utf8'));

tracker.regions.france.candidates += 24;
tracker.regions.france.ideas += 4;
tracker.total_candidates += 24;
tracker.total_ideas += 4;
tracker.total_rejected += 20;

// Update categories_recent - add health-wellness and keep last 5
tracker.categories_recent.unshift('health-wellness');
if (tracker.categories_recent.length > 5) {
  tracker.categories_recent = tracker.categories_recent.slice(0, 5);
}

fs.writeFileSync('regions-tracker.json', JSON.stringify(tracker, null, 2));
console.log('Updated tracker for France wellness run');
