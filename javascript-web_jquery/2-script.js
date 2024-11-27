#!/usr/bin/node
$(document).ready(function() {
  // use core from file 1
  // use click and specify red_header div
  $('red_header').click(function() {
    $('header').css('color', '#FF0000');
    });
});
