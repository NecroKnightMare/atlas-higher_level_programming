#!/usr/bin/node
// square class that inherits from file 5 Sq
// made function and extended class, charprint is in the class
const Square = require('./5-square.js');

class SquareChar extends Square {
  charprint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = SquareChar;
