#!/usr/bin/node

const process = require('process');
if (process.argv.length == 1) {
    console.log('Argument found');
    console.log(process.argv);
}
else {
    console.log('No argument');
}
