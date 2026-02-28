const fs = require('fs');
const tracker = JSON.parse(fs.readFileSync('regions-tracker.json', 'utf8'));

tracker.regions.italy.candidates += 20;
tracker.regions.italy.ideas += 4;
tracker.total_candidates += 20;
tracker.total_ideas += 4;
tracker.total_rejected += 16;

// Update categories_recent - keep last 5
tracker.categories_recent.push('health-wellness');
if (tracker.categories_recent.length > 5) {
  tracker.categories_recent.shift();
}

fs.writeFileSync('regions-tracker.json', JSON.stringify(tracker, null, 2));
console.log('Tracker updated: Italy +20 candidates, +4 ideas, +16 rejected');
