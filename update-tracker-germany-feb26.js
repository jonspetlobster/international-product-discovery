const fs = require('fs');
const tracker = JSON.parse(fs.readFileSync('regions-tracker.json', 'utf8'));

tracker.regions.germany.candidates += 23;
tracker.regions.germany.ideas += 3;
tracker.total_candidates += 23;
tracker.total_ideas += 3;

// Update categories_recent (keep last 5, add new, remove oldest if >5)
tracker.categories_recent.push('baby-kids');
if (tracker.categories_recent.length > 5) {
  tracker.categories_recent.shift();
}

fs.writeFileSync('regions-tracker.json', JSON.stringify(tracker, null, 2));
console.log('✅ Updated tracker: Germany +23 candidates, +3 ideas');
