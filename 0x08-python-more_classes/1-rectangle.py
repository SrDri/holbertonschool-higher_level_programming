#!/usr/bin/python3


class Rectangle:
    """Class rectangle"""

    def __init__(self, width=0, height=0):
        """Constructor-Arguments:
            width: width-rectangle
            height: height-rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter"""
        if isinstance(value, int) is not True:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter"""
        if isinstance(value, int) is not True:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
