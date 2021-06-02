#!/usr/bin/python3
""" write_file function """


def write_file(filename="", text=""):
    """ write """
    with open(filename, mode="w", encoding="utf-8") as a_file:
        return a_file.write(text)
