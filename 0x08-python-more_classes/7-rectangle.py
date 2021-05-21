#!/usr/bin/python3
"""Module Rectangle"""


class Rectangle:
    """Class rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Constructor-Arguments:
            width: width-rectangle
            height: height-rectangle
        """
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    def __str__(self):
        """# character"""
        aux = ""
        str(self.print_symbol)

        if self.__height == 0 or self.__width == 0:
            return aux

        for i in range(0, self.__height):
            aux = aux + "{}".format(self.__width * self.print_symbol)

            if i + 1 != self.__height:
                aux = aux + "\n"

        return aux

    def __repr__(self):
        """representations rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Delete rectangle class"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

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

    def area(self):
        """area of rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """perimeter of rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0

        return self.__height * 2 + self.__width * 2
