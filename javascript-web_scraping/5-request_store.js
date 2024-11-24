#!/usr/bin/node
// Write a script that gets the contents of a webpage and stores it in a file
const request = require('request');
// file system module request 'fs'
const fs = require('fs');
// grab url argument
const url = process.argv[2];
// grab file path to store later in code
const file = process.argv[3];
request(url, (err, response, body) => {
    if (err) {
      console.error(err);
      return;
    }
    fs.writeFile(filepath, body, 'utf-8', (err) => {
      if (err) {
        console.error(err);
        return;
      }
    });
});
