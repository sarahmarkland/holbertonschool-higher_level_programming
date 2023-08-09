#!/usr/bin/node
// Write a class Rectangle that defines a rectangle:
// You must use the class notation for defining your class
// The constructor must take 2 arguments w and h
// If w or h is equal to 0 or not a positive integer, create an empty 
// object
// Create an instance method called print() that prints the rectangle
// using the character X
// Create an instance method called rotate() that exchanges the width
// and the height of the rectangle
// Create an instance method called double() that multiples the width
// and the height of the rectangle by 2

class Rectangle {
    constructor (w, h) {
        if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
        } else {
        this.width = w;
        this.height = h;
        }
    }
    
    print () {
        const row = 'X'.repeat(this.width);
        for (let i = 0; i < this.height; i++) {
        console.log(row);
        }
    }
    
    rotate () {
        const temp = this.width;
        this.width = this.height;
        this.height = temp;
    }
    
    double () {
        this.width *= 2;
        this.height *= 2;
    }
    }
