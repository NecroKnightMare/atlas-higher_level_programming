#!/usr/bin/node
// Write a script that prints the title of a Star Wars movie
// where the episode number matches a given integer.

// You must use the module request
const request = require('request');
// https://swapi-api.hbtn.io/api/
//  endpoint https://swapi-api.hbtn.io/api/films/${movieID};
const movie = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movie}`;
request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const data = JSON.parse(body);
  console.log(data.title);
});
