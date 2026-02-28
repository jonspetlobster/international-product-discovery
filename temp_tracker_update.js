const fs = require('fs');
const tracker = JSON.parse(fs.readFileSync('regions-tracker.json', 'utf8'));

tracker.regions.colombia.candidates += 22;
tracker.regions.colombia.ideas += 3;
tracker.total_candidates += 22;
tracker.total_ideas += 3;

// Update categories_recent - keep last 5, add condiments-sauces
tracker.categories_recent.push('condiments-sauces');
if (tracker.categories_recent.length > 5) {
  tracker.categories_recent = tracker.categories_recent.slice(-5);
}

fs.writeFileSync('regions-tracker.json', JSON.stringify(tracker, null, 2));
console.log('Updated tracker: colombia +22 candidates, +3 ideas');
