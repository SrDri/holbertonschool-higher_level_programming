#!/usr/bin/node

const n_array = process.argv.slice(2);
const lenght_array = n_array.length;
if ((lenght_array) < 2) {
	console.log('0');
} else {
	n_array.sort((x, y) => x - y);
	console.log(n_array[lenght_array - 2]);
}
