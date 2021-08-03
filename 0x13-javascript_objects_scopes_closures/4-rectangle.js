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

	rotate() {
		let aux = this.width;
		this.width = this.height;
		this.height = aux;
	}

	double() {
		this.width = this.width * 2;
		this.height = this.height * 2;
	}
};
