const fs = require('fs');
const tracker = JSON.parse(fs.readFileSync('regions-tracker.json', 'utf8'));

tracker.regions.netherlands.candidates += 20;
tracker.regions.netherlands.ideas += 3;
tracker.total_candidates += 20;
tracker.total_ideas += 3;

// Update categories_recent - add fitness, remove oldest if >5
tracker.categories_recent.push('fitness');
if (tracker.categories_recent.length > 5) {
  tracker.categories_recent.shift();
}

fs.writeFileSync('regions-tracker.json', JSON.stringify(tracker, null, 2));
console.log('Updated tracker');
