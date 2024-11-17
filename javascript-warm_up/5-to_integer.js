#!/usr/bin/node
// if string converts to int, will print if statement else it isn't an integer
const process = require('process');
const arg = process.argv[2];
const stringToInt = parseInt(arg);
if (!isNaN(stringToInt)) {
console.log('My number: <first argument converted in integer></first>');
} else {
console.log('Not a number');
}
