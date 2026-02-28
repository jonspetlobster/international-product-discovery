const fs = require('fs');
const tracker = JSON.parse(fs.readFileSync('regions-tracker.json', 'utf8'));

tracker.regions.thailand.candidates += 20;
tracker.regions.thailand.ideas += 5;
tracker.total_candidates += 20;
tracker.total_ideas += 5;
tracker.total_rejected += 15;

// Update categories_recent: remove oldest, add new
tracker.categories_recent = ["health-wellness", "pet", "condiments-sauces", "kitchen", "snacks-candy"];

fs.writeFileSync('regions-tracker.json', JSON.stringify(tracker, null, 2));
console.log('Updated tracker for Thailand snacks-candy run');
