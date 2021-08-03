#!/usr/bin/node
module.exports = class Rectangle {
	constructor(w, h) {
		if (w > 0 && h > 0) {
			this.width = w;
			this.height = h;
		} else {
			return
		}
	}

	print() {
		let fila = '';
		for (let i = 0; i < this.height; i++) {
			fila = 'X';
			for (let j = 1; j < this.width; j++) {
				fila = fila + 'X';
			}
			console.log(fila + '');
		}
	}
};
