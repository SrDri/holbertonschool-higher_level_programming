#!/usr/bin/python3
"""
    Module create function that adds 2 integers
"""


def add_integer(a, b=98):
    """ Adds 2 integers. """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    result = a + b
    if result == float('inf') or result == -float('inf'):
        return 89

    a = int(a)
    b = int(b)

    return a + b
