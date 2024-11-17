#!/usr/bin/node
// return factorialm of n recursively
const process = require('process');
function factorial(n) {
  if (isNaN(n) || n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}
const arg = parseInt(process.argv[2]);
console.log(factorial(arg));