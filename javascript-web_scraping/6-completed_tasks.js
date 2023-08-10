#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const dict = {};
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    for (let i = 0; i < data.length; i++) {
      if (data[i].completed === true) {
        if (data[i].userId in dict) {
          dict[data[i].userId] += 1;
        } else {
          dict[data[i].userId] = 1;
        }
      }
    }
    console.log(dict);
  }
});
