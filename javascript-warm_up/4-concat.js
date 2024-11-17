#!/usr/bin/node
// print two args passed using "is"

const process = require('process');

if (process.argv.length > 4) {
    const arg1 = process.argv[2];
    const arg2 = process.argv[3];
    const arg3 = "is"
    console.log(arg1, arg3, arg2)
}
else if (process.argv[1]) {
    // console.log('Argument found'); don't need this for the checker
    const arg1 = process.argv[2];
    const arg2 = process.argv[3];
    const arg3 = "is"
    console.log(arg1, arg3, arg2)
}
else {
    console.log('No argument');
}
