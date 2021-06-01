#!/usr/bin/python3
""" inherits_from function """


def inherits_from(obj, a_class):
    """ Instance class """

    result = issubclass(type(obj), a_class) and type(obj) is not a_class

    return(result)
