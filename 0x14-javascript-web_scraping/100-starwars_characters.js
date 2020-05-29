#!/usr/bin/node
let request = require('request');
request.get('http://swapi.co/api/films/' + process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    for (let chars of JSON.parse(body).characters) {
      request.get(chars, function (error, response, body) {
        if (error) {
          console.log(error);
        } else if (response.statusCode === 200) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
