#!/usr/bin/node
// 
const process = require('process');
const arg = process.argv[2];
const size = parseInt(arg);
if (isNaN(size)) {
    console.log('Missing number of occurrences');
  } else {
    for (let x = 0; x < size; x++) {
      console.log('x');
    }
  }