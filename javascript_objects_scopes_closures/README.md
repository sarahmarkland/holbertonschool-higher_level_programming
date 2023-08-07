Readme for JavaScript Objects, Scopes, Closures
# General

## Why JavaScript programming is amazing
## How to create an object in JavaScript
Common Approaches
- Object Literal: displays key-val pairs within curly braces
- Constructor Function: blueprint for creating objs with similar properties and methods
- Object.create() method: allows you to create a new object with a specified prototype object.
- ES6 Class:
ES6 introduced classes that make object creation more structured and easier to manage.


```
class Person {
constructor(name, age, gender) {
    this.name = name;
    this.age = age;
    this.gender = gender;
}
}

const person = new Person('John Doe', 30, 'male');
```
## What this means
In JavaScript, *this* is a special keyword that refers to the context in which a function is called. The value of *this* changes based on how a function is invoked, and it is dynamically determined at runtime. The behavior of *this* can be a bit tricky and might lead to confusion for new JavaScript developers.
1. Global Scope: referenced outside of a function or obj, it refers to the global obj. In a web browser env, the global obj is typically `window`
2. Function Invocation: used inside a regular function (not method of an obj or arrow func) if refers to the global obj or `undefined`
3. Method Invocation: used inside a method of an object, it refers to the object that owns the method
## What undefined means
special value that represents the absence of a meaningful value. When a variable is declared but not assigned a value, or when a function does not explicitly return a value, it is automatically assigned the value `undefined`
## Why the variable type and scope is important
## What is a closure
A closure is a powerful and fundamental concept in JavaScript, which arises when a function is defined inside another function and retains access to the variables and scope of its parent (enclosing) function, even after the parent function has finished executing. In other words, a closure "closes over" its environment, capturing and preserving the variables and values in its lexical scope.

Closures are created in the following situations:

    1. When a function is defined inside another function.
    2. When the inner function references variables from the outer (enclosing) function's scope.
## What is a prototype
In JavaScript, a prototype is an internal property of every object that allows objects to share methods and properties with other objects. Every object in JavaScript has a prototype, which is used to look up properties and methods that are not directly defined on the object itself.
## How to inherit an object from another
In JavaScript, you can achieve inheritance between objects using either prototype-based inheritance or class-based inheritance (introduced in ECMAScript 6 with the class syntax). 