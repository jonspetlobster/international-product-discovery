const fs = require('fs');
const tracker = JSON.parse(fs.readFileSync('regions-tracker.json', 'utf8'));

tracker.regions.uk.candidates += 4; // 4 valid candidates that weren't rejected
tracker.regions.uk.ideas += 4; // 4 validated ideas
tracker.categories_recent.push('snacks-candy');
if (tracker.categories_recent.length > 5) tracker.categories_recent.shift();
tracker.total_candidates += 4;
tracker.total_ideas += 4;

fs.writeFileSync('regions-tracker.json', JSON.stringify(tracker, null, 2));
console.log('Tracker updated: UK +4 candidates, +4 ideas');
