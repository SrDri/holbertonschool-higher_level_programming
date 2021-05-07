#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):

    sort_key = sorted(set(a_dictionary))

    for key in sort_key:
        print("{:s}: {}".format(key, a_dictionary[key]))
