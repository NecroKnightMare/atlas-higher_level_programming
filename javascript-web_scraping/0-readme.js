#!/usr/bin/node
// Write a script that reads and prints the content of a file.
const fs = require('fs');
// The first argument is the file path
const filePath = process.argv[2];
// The content of the file must be read in utf-8
fs.readFile(filePath, 'utf-8', (err, data) => {
// If an error occurred during the reading, print the error object
  if (err) {
  console.error(err);
    return;
  }
  console.log(data);
});
