#!/usr/bin/node
// square class that inherits from Rectangle
const Square = require('./5-square');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
