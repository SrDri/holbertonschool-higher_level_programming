#!/usr/bin/node
// status code

const request = require('request');

request.get(process.argv[2], function (error, response) {
  if (error) {
    throw error;
  }
  console.log('code: ' + response.statusCode);
});
