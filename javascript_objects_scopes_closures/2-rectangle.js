#!/usr/bin/node
// Write a class Rectangle that defines a rectangle:
// You must use the class notation for defining your class
// The constructor must take 2 arguments w and h
// If w or h is equal to 0 or not a positive integer, create an empty object

class Rectangle {
  constructor (w, h) {
    if (w === undefined || h === undefined) {
      return;
    }
    if (w <= 0 || h <= 0) {
      return;
    }
    this.width = w;
    this.height = h;
  }
}
