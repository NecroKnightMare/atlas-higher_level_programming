#!/usr/bin/node
// add instance to print X
class Rectangle {
    constructor (w, h) {
      if (w > 0 && h > 0) {
        this.width = w;
        this.height = h;
        print('X', w, h);
      }
    }
  }
  module.exports = Rectangle;
  