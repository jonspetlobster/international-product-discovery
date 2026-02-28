const fs = require('fs');
const tracker = JSON.parse(fs.readFileSync('regions-tracker.json', 'utf8'));

// Update Turkey region
tracker.regions.turkey.candidates += 23;
tracker.regions.turkey.ideas += 5;

// Update categories_recent (keep last 5, add new one)
tracker.categories_recent.push('laundry-clothing');
if (tracker.categories_recent.length > 5) {
  tracker.categories_recent.shift();
}

// Update totals
tracker.total_candidates += 23;
tracker.total_ideas += 5;
tracker.total_rejected += 18;

fs.writeFileSync('regions-tracker.json', JSON.stringify(tracker, null, 2));
console.log('Updated tracker: Turkey +23 candidates, +5 ideas, +18 rejected');
