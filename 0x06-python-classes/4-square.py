#!/usr/bin/python3
"""Module Square"""


class Square:
    """class"""

    def __init__(self, size=0):
        """Constructor"""
        self.size = size

    @property
    def size(self):
        """get __size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set __size"""
        if value:
            if isinstance(value, int) is not True:
                raise TypeError("size must be an integer")
                return

            if value < 0:
                raise ValueError("size must be >= 0")
                return

        self.__size = value

    def area(self):
        """Return size"""
        return self.__size ** 2
