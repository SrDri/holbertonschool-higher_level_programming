#!/usr/bin/python3

def no_c(my_string):

	rm = ""

    for _c in my_string:
        if _c is "c" or _c is "C":
            continue

        rm = rm + _c

    return rm
