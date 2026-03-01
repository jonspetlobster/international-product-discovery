const fs = require('fs');
const tracker = JSON.parse(fs.readFileSync('regions-tracker.json', 'utf8'));

tracker.regions.new_zealand.candidates += 24;
tracker.regions.new_zealand.ideas += 3;
tracker.total_candidates += 24;
tracker.total_ideas += 3;
tracker.total_rejected += 6;

// Update categories_recent (keep last 5)
tracker.categories_recent.push('personal-care');
if (tracker.categories_recent.length > 5) {
  tracker.categories_recent.shift();
}

fs.writeFileSync('regions-tracker.json', JSON.stringify(tracker, null, 2));
console.log('Updated tracker: NZ +24 candidates, +3 ideas, +6 rejected');
