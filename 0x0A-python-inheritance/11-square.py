#!/usr/bin/python3
""" Square class """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ The Square class """

    def __init__(self, size):
        """ Constructor class """

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """ Print method """
        return "[Square] {0:d}/{0:d}".format(self.__size)

    def area(self):
        """ Area the square """

        return self.__size * self.__size
