#!/usr/bin/node
// 
const process = require('process');
const arg = process.argv[2];
const size = parseInt(arg);
if (isNaN(size)) {
    console.log('Missing number of occurrences');
  } else {
    for (let row = 0; row < size; row++) {
      console.log('x', row);
      for (let col = 0; col < size; col++) {
        console.log('x', col);
    }
  }
}
