#!/usr/bin/python3
""" MyList class """


class MyList(list):
    """ inherits from the list """

    def print_sorted(self):
        """ Print list sorted order """
        print(sorted(self))
