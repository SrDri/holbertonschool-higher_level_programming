#!/usr/bin/python3
""" lookup function """


def lookup(obj):
    """ returns all properties and methods """

    list_aux = []

    for i in dir(obj):
        list_aux.append(i)

    return list_aux
