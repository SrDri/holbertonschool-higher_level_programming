#!/usr/bin/node

const { argv } = require('process');

if (isNaN(argv[2]) || !argv[2]) {
  console.log('Missing size');
} else {
  let fila = '';
  for (let i = 0; i < argv[2]; i++) {
    fila = '';
    for (let j = 0; j < argv[2]; j++) {
      fila = fila + 'X';
    }
    console.log(fila + '');
  }
}
