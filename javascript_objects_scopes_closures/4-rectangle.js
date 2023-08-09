#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w >= 1 && h >= 1) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;
    let j = 0;
    let string = '';
    for (; i < this.width; i++) {
      string += 'X';
    }
    for (; j < this.height; j++) {
      console.log(string);
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
}
module.exports = Rectangle;
