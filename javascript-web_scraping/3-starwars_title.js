#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const web = 'https://swapi-api.hbtn.io/api/films/' + url;
request(web, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const json = JSON.parse(body);
    console.log(json.title);
  }
});
