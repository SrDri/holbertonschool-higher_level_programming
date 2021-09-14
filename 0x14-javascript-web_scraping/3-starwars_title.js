#!/usr/bin/node
// request api

const request = require('request');

request.get('http://swapi.co/api/films/' + process.argv[2], (error, req, body) => {
  if (error) {
    throw error;
  }

  console.log(JSON.parse(body).title);
});
