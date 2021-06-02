#!/usr/bin/python3
""" `Rectangle` class """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ The Rectangle class """

    def __init__(self, width, height):
        """ Constructor class """
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """ Print method """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

    def area(self):
        """ Area the square """
        return self.__height * self.__width
