#!/usr/bin/node
// passing process as value to print if else conditions
const process = require('process');
if (process.argv.length > 2) {
    console.log('Argument found');
    console.log(process.argv);
}
else {
    console.log('No argument');
}
