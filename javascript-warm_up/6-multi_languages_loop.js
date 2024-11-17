#!/usr/bin/node
// prints array of strings in order with while loop
const process = require('process');
const arg = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
while (arg) {
  console.log(arg[0], arg[1], arg[2]);
} 