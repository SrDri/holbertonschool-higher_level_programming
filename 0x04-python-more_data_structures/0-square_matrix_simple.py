#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    new = []

    for elem in matrix:
        new.append(list(map(lambda x: x**2, elem)))

    return new
