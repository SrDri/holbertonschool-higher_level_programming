#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):

    for elem in matrix:
        print(" ".join(["{:d}".format(n) for n in elem]))
