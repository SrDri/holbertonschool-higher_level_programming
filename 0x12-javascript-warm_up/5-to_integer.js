#!/usr/bin/node

const { argv } = require('process');

if (isNaN(argv[2]) === false) {
  console.log('My number: ' + argv[2]);
} else {
  console.log('Not a number');
}
