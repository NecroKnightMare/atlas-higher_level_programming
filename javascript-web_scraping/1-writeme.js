#!/usr/bin/node
// Write a script that writes a string to the file
const fs = require('fs');
// The first argument is the file path
const filePath = process.argv[2];
// string argument
const phrase = process.argv[3];
// The content of the file must be read in utf-8
// added encoding, thinks string is being interpreted as the encoder
fs.writeFile(filePath, phrase, { encoding: 'utf-8' }, (err) => {
// If an error occurred during the reading, print the error object
  if (err) {
    console.error(err);
  }
});
