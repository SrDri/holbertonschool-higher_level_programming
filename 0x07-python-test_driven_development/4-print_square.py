#!/usr/bin/python3
"""
    Module create function that print square
"""


def print_square(size):
    """ print # in size """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if float(size) < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print("#", end="")

        print()
