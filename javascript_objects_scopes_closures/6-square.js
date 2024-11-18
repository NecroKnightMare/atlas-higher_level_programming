#!/usr/bin/node
// square class that inherits from Rectangle
const Square = require('./5-square.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

charprint (c) {
  if (c === undefined) {
    console.log('X');
  }
}
module.exports = Square;
