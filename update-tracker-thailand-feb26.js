const fs = require('fs');
const tracker = JSON.parse(fs.readFileSync('regions-tracker.json', 'utf8'));

// Thailand is position 4 in the array (0-indexed)
const thailandIndex = 4;
tracker.regions[thailandIndex].candidates += 22;
tracker.regions[thailandIndex].ideas += 3;

// Update recent categories (keep last 5)
tracker.categories_recent.push('grocery-pantry');
if (tracker.categories_recent.length > 5) {
  tracker.categories_recent.shift();
}

tracker.total_candidates += 22;
tracker.total_ideas += 3;

fs.writeFileSync('regions-tracker.json', JSON.stringify(tracker, null, 2));
console.log('Tracker updated: Thailand +22 candidates, +3 ideas');
