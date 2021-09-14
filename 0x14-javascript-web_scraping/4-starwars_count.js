#!/usr/bin/node
// request api.

const request = require('request');

request.get(process.argv[2], (error, req, body) => {
	if (error) {
		throw error;
	}
	const resultado = JSON.parse(body).results;

	let counter = 0;

	resultado.forEach(element => {
		element.characters.forEach(char => {
			let id = char.slice(-3, -1).replace('/', '');
			id = parseInt(id);
			if (id === 18) {
				counter++;
			}
		});
	});
	console.log(counter);
});
