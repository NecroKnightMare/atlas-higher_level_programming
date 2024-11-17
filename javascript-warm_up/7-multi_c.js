#!/usr/bin/node
// repeats string by x if string is integer
const process = require('process');
const arg = process.argv[2];
const stringToInt = parseInt(arg);
const x = stringToInt * x;
while (!isNaN(stringToInt)) {
  console.log(stringToInt, x);
}
console.log('Missing number of occurrences');
