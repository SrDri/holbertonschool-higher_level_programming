#!/usr/bin/node
// request api.

const request = require('request');

request.get(process.argv[2], (error, req, body) => {
  if (error) {
    throw error;
  }
  const resultado = JSON.parse(body);

  const dict = {};

  resultado.forEach(element => {
    if (element.completed === true) {
      console.log("#### AQUI ### " + dict[element.userId])
      if (dict[element.userId] === undefined) {
        dict[element.userId] = 0;

      }
      dict[element.userId]++;
    }
  });
  console.log(dict);
});
