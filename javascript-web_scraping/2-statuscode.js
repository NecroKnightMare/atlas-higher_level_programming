#!/usr/bin/node
// Write a script that display the status code of a GET request.
// You must use the module request
const request = require('request');
// The first argument is the URL to request (GET)
// https://intranet.hbtn.io/status
const url = process.argv[2];
// The status code must be printed like this: code: <status code>
request(url, (err, response) => {
  if (err) {
    console.log(err);
    console.log(response.statusCode);
  }
});
