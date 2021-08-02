#!/usr/bin/node

const { argv } = require('process');

const a = parseInt(argv[2]);

function factorial (a) {
  if (isNaN(a) || a === 1) {
    return (1);
  } else {
    return a * factorial(a - 1);
  }
}
console.log(factorial(a));
