#!/usr/bin/python3
"""
    Module create function text indentation
"""


def text_indentation(text):
    """
    replace space, ., ? with new line.
    """
    if not isinstance(text, str) or text == None:
        raise TypeError("text must be a string")

    if text == "":
        print("")
        return

    text = text.replace(".", ".\n\n")
    text = text.replace("?", "?\n\n")
    text = text.replace(":", ":\n\n")

    remove_init_spaces = "\n".join(i.lstrip() for i in text.split("\n"))

    print(remove_init_spaces, end="")
