#!/usr/bin/node
const request = require('request');
const options = {
  url: 'http://swapi.co/api/films/' + process.argv[2],
  method: 'GET'
};
request(options, function (error, response, body) {
  if (error) {
    return console.log(error);
  } else {
    let charList = JSON.parse(body).characters;
    charList.forEach(function (element) {
      request(element, function (error, response, body) {
        if (error) {
          return console.log(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
