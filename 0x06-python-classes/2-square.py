#!/usr/bin/python3
"""Module Square"""


class Square:
    """class"""

    def __init__(self, size=0):
        """Constructor"""

        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
            return

        if size < 0:
            raise ValueError("size must be >= 0")
            return

        self.__size = size
