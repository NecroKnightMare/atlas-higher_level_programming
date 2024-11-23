#!/usr/bin/node
// Write a script that prints the number of movies
// where the character “Wedge Antilles” is present.
const request = require('request');
const movie = process.argv[2];
// API URL
const url = `https://swapi-api.hbtn.io/api/people/${character}`;
// Wedge Antilles character
const character = '18';
request(movie, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const films = JSON.parse(body).results;
  const wedgeAntilles = films.filter(film =>
    film.characters.includes(url));
// grab length of wedge Antilles movies that are present
  console.log(wedgeAntilles.length);
});
