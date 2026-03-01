const fs = require('fs');
const tracker = JSON.parse(fs.readFileSync('regions-tracker.json', 'utf8'));

tracker.regions.sweden.candidates += 25;
tracker.regions.sweden.ideas += 5;
tracker.total_candidates += 25;
tracker.total_ideas += 5;
tracker.total_rejected += 20;

tracker.categories_recent.shift();
tracker.categories_recent.push('kitchen');

fs.writeFileSync('regions-tracker.json', JSON.stringify(tracker, null, 2));
console.log('Updated tracker for Sweden kitchen run');
