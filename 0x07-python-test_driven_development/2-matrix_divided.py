#!/usr/bin/python3
"""
    Module create function that divided matrix
    @matrix: a matrix
    @div: number to divide
"""


def matrix_divided(matrix, div):
    """ Matrix divided by the number """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_list = []
    sep_i = 0
    for iter in matrix:
        if not isinstance(iter, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

        new_list.append([])

        for n in iter:
            if not isinstance(n, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")

            result = round(n / div, 2)
            new_list[sep_i].append(result)

        sep_i = sep_i + 1

    size = len(matrix[0])
    for row in matrix:
        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")

    return new_list
