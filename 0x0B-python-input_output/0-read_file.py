#!/usr/bin/python3
""" read_file function """


def read_file(filename=""):
    """ read text file """
    with open(filename, mode="r", encoding="utf-8") as a_file:
        print(a_file.read(), end="")
