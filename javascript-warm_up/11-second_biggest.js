#!/usr/bin/node
// find and print secong largest integer
const process = require('process');
// slice - returns a copy of an array
// map - returns array that contains nuumber
// sort - sorts largest and second largest
const args = process.argv.slice(2).map(Number).sort((a, b) => b - a);

if (args.length <= 1) {
  console.log(0);
} else {
    console.log(args[1]);
}
