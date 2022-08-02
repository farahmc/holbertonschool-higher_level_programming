#!/usr/bin/node

const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let i = 0; i < this.width; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
