const fs = require('fs');
const tracker = JSON.parse(fs.readFileSync('regions-tracker.json', 'utf8'));

tracker.regions.indonesia.candidates += 21;
tracker.regions.indonesia.ideas += 5;
tracker.total_candidates += 21;
tracker.total_ideas += 5;

// Update categories_recent (keep last 5)
tracker.categories_recent.push('snacks-candy');
if (tracker.categories_recent.length > 5) {
  tracker.categories_recent.shift();
}

fs.writeFileSync('regions-tracker.json', JSON.stringify(tracker, null, 2));
console.log('Updated tracker: indonesia +21 candidates, +5 ideas');
