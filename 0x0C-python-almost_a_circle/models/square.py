#!/usr/bin/python3
""" Module Square class """
from .rectangle import Rectangle


class Square(Rectangle):
    """ The Square class """

    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor Square class """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ Prints """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """ updates the argumuments """
        if len(args):
            for c, argum in enumerate(args):
                if c == 0:
                    self.id = argum
                if c == 1:
                    self.size = argum
                if c == 2:
                    self.x = argum
                if c == 3:
                    self.y = argum
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """ returns the dictionary representation """
        aux = {}
        for key, val in self.__dict__.items():
            key = key.replace("_Rectangle__", "")
            if key == "width":
                key = "size"
            else:
                key

            if key == "height":
                continue

            aux[key] = val

        return aux

    @property
    def size(self):
        """ Size getter """
        return self.width

    @size.setter
    def size(self, valor):
        """ Size setter """
        self.width = valor
        self.height = valor
