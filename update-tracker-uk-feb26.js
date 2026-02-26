const fs = require('fs');
const tracker = JSON.parse(fs.readFileSync('regions-tracker.json', 'utf8'));

tracker.regions.uk.candidates += 20;
tracker.regions.uk.ideas += 4;
tracker.total_candidates += 20;
tracker.total_ideas += 4;

// Update categories_recent (keep last 5)
tracker.categories_recent.push('health-wellness');
if (tracker.categories_recent.length > 5) {
  tracker.categories_recent.shift();
}

fs.writeFileSync('regions-tracker.json', JSON.stringify(tracker, null, 2));
console.log('Updated tracker: UK +20 candidates, +4 ideas');
