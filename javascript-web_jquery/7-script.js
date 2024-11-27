#!/usr/bin/node
$(document).ready(function() {
  //use get for api and data retrieved from function
  $.get(`https://swapi-api.hbtn.io/api/people/5/?format=json`, function(data) {
    //  core function to get character data from star wars API
    $('#character').text(data.name);
  });
});
