#!/usr/bin/node
$(document).ready(function() {
  //use get for api and data retrieved from function
  $.get(`https://swapi-api.hbtn.io/api/films/?format=json`, function(data) {
    // movie variable to get results
    const movies = data.results;
    // iterate movies
    movies.forEach(function(movie) {
      //  core function to append movie titles to list
      $('#list_movies').append('<li>' + movie.title + '</li>');
    });
  });
});
