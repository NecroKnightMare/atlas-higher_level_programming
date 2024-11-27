#!/usr/bin/node
$(document).ready(function() {
  // when add_item is clicked add list item
  $('#add_item').click(function() {
    $('.mylist').append('<li>Item</li>');
  });
});
