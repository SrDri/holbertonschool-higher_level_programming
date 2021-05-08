#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    new = {}

    for key, num in a_dictionary.items():
        new[key] = num * 2

    return new
