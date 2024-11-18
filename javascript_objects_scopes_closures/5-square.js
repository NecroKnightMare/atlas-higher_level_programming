#!/usr/bin/node
// square class that inherits from Rectangle
const Rectangle = require('./4-rectangle')

class Square extends Rectangle {
  constructor (size) {
    super(size);
  }
}

module.exports = Square;
