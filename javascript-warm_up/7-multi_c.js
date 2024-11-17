#!/usr/bin/node
// repeats string by x if string is integer
const process = require('process');
const arg = process.argv[2];
const stringToInt = parseInt(arg);
 for (let x = 0; x < stringToInt; x++) {
  console.log(stringToInt, x);
}
if (isNaN(stringToInt)) {
  console.log('Missing number of occurrences');
}
