#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const completed = {};
    for (const task of JSON.parse(body)) {
      if (task.completed === true) {
        if (task.userId in completed) { completed[task.userId]++; } else { completed[task.userId] = 1; }
      }
    }
    console.log(completed);
  }
});
