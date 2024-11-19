#!/usr/bin/node
//  prints first argument and doesn't use length
const process = require('process');
if (process.argv[2]) {
  // console.log('Argument found'); don't need this for the checker
  console.log(process.argv[2]);
} else if (process.argv[2]) {
  console.log('Arguments found');
  // console.log(process.argv); didn't need to print but this is how
} else {
  console.log('No argument');
}
