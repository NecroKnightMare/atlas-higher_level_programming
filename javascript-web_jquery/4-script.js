#!/usr/bin/node
$(document).ready(function() {
  // use click to activate event to toggle
  $('#toggle_header').click(function() {
    // if header is red or green do the following
    if ($('header').hasClass('red')) {
      // if red remove and add green
      $('header').removeClass('red').addClass('green');
    } else {
      $('header').removeClass('green').addClass('red');
    }  
  });
});
