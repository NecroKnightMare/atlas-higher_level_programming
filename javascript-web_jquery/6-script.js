#!/usr/bin/node
$(document).ready(function() {
  //use click function for update_header 
  $('#update_header').click(function() {
    // change header to New Header!!!
    $('header').text('New Header!!!');
  });
});
