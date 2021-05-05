#!/usr/bin/python3


def no_c(my_string):

    rm = ""

    for charc in my_string:
        if charc is "c" or charc is "C":
            continue

        rm = rm + charc

    return rm
