#!/usr/bin/node
// same as file 2 but prints first argument
const process = require('process');
if (process.argv.length == 1) {
    console.log('Argument found');
    console.log(process.argv);
}
else if (process.argv.length > 2) {
    console.log('Arguments found');
    // console.log(process.argv); didn't need to print but this is how
}
else {
    console.log('No argument');
}
