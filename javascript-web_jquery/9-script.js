#!/usr/bin/node
// fetches from https://hellosalut.stefanbohacek.dev/?lang=fr
// and displays the value of hello from that fetch in the HTML tag DIV#hello
$(document).ready(function() {
  //use get for api and data retrieved from function
  $.get(`https://hellosalut.stefanbohacek.dev/?lang=fr`, function(data) {
    //  core function to get value of hello
    $('#hello').text(data.hello);
  });
});
  