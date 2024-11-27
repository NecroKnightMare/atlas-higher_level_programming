#!/usr/bin/node
// Write a script that prints the number of movies
// where the character “Wedge Antilles” is present.
const request = require('request');
const movie = process.argv[2];
// Wedge Antilles character
const character = '18';
// API URL
// const url = `https://swapi-api.hbtn.io/api/people/18`;
request(movie, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const films = JSON.parse(body).results;
  let count = 0;

  films.forEach((film) => {
    if (film.characters.some(characterUrl => characterUrl.includes(character))) {
      count++;
    }
  });
  // grab count of wedge Antilles movies that are present
  console.log(count);
});
