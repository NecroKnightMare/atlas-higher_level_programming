#!/usr/bin/node
//  prints first argument and doesn't use length
const process = require('process');
if (process.argv[1]) {
    console.log('Argument found');
    console.log(process.argv[1]);
}
else if (process.argv[2]) {
    console.log('Arguments found');
    // console.log(process.argv); didn't need to print but this is how
}
else {
    console.log('No argument');
}
