const fs = require('fs');

const puzzleText = fs.readFileSync('sources/puzzleinput_1.txt', 'utf8');
const puzzleList = puzzleText.split('\n');

let leftIds = [];
let rightIds = [];

for (const ids of puzzleList) {
  leftLocationId = ids.split('   ')[0];
  rightLocationId = ids.split('   ')[1];
  leftIds.push(leftLocationId);
  rightIds.push(rightLocationId);
}

leftIds.sort((a, b) => a - b);
rightIds.sort((a, b) => a - b);
let distances = [];
let dist = 0;

for (let i = 0; i < puzzleList.length; i++) {
    dist = Math.abs(leftIds[i] - rightIds[i]);
    distances.push(dist);
  }

let totalDistance = distances.reduce((accumulator, currentValue) => accumulator + currentValue, 0);

console.log(totalDistance);
let similarityScores = [];

for (const leftId of leftIds) {
    occurences = rightIds.filter(rightId => rightId === leftId).length;
    similarityScores.push(leftId * occurences);
  };

let totalSimilarities = similarityScores.reduce((accumulator, currentValue) => accumulator + currentValue, 0);

console.log(totalSimilarities);
