#!/usr/bin/node

const { argv } = require('process');

const a = argv[2];
const b = argv[3];

function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    return (NaN);
  } else {
    return parseInt(a) + parseInt(b);
  }
}
console.log(add(a, b));
