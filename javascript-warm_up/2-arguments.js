#!/usr/bin/node
// passing process as value to print if else conditions
const process = require('process');
if (process.argv.length == 3) {
    console.log('Argument found');
}
else if (process.argv.length > 3) {
    console.log('Arguments found');
    // console.log(process.argv); didn't need to print but this is how
}
else {
    console.log('No argument');
}
