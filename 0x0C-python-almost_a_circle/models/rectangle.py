#!/usr/bin/python3
""" Module Rectangle class """
from .base import Base


class Rectangle(Base):
    """ The Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Init Rectangle class """
        super().__init__(id=id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # Task 6 - main 5
    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

    # Task 4 - main 3
    def area(self):
        return self.__width * self.__height

    # Task 5 and 7 - main 4, 6
    def display(self):
        for eje_y in range(self.y):
            print("")

        for i in range(0, self.__height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args):
        """ Update arguments """
        for argum, c in zip(args, range(5)):
            if c == 0:
                self.id = argum
            if c == 1:
                self.width = argum
            if c == 2:
                self.height = argum
            if c == 3:
                self.x = argum
            if c == 4:
                self.y = argum
            if c == None:
                break

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, valor):
        if not isinstance(valor, int):
            raise TypeError("width must be an integer")

        if valor <= 0:
            raise ValueError("width must be > 0")

        self.__width = valor

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, valor):
        if not isinstance(valor, int):
            raise TypeError("height must be an integer")

        if valor <= 0:
            raise ValueError("height must be > 0")

        self.__height = valor

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, valor):
        if not isinstance(valor, int):
            raise TypeError("x must be an integer")

        if valor < 0:
            raise ValueError("x must be >= 0")

        self.__x = valor

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, valor):
        if not isinstance(valor, int):
            raise TypeError("y must be an integer")

        if valor < 0:
            raise ValueError("y must be >= 0")

        self.__y = valor
