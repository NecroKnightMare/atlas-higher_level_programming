#!/usr/bin/node
// passing process as value to print if else conditions
const process = require('process');
if (process.argv.length > 2) {
    console.log('Argument found');
    // console.log(process.argv); didn't need to print nut this is how
}
else {
    console.log('No argument');
}
