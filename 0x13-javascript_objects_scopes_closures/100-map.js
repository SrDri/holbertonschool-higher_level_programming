#!/usr/bin/node
const lista = require('./100-data').list;

console.log(lista);
console.log(lista.map((el, idx) => el * idx));
