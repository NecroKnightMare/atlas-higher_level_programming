#!/usr/bin/node
// print sum of a + b
const process = require('process');
function add(a, b) {
    return a + b;
}
const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);
if (isNaN(arg1) || isNaN(arg2)) {
    console.log('NaN');
} else {
    console.log(arg1 + arg2);
}
