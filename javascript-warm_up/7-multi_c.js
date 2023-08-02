#!/usr/bin/node
const string = 'C is fun';

if (process.argv[2] && !isNaN(process.argv[2])) {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log(string);
  }
  process.exit();
} else {
  console.log('Missing number of occurrences');
}
