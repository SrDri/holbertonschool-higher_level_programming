#!/usr/bin/python3
""" append_file function """


def append_write(filename="", text=""):
    """ write """
    with open(filename, mode="a", encoding="utf-8") as app_file:
        return app_file.write(text)
