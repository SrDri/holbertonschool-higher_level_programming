#!/usr/bin/python3
""" is_kind_of_class function """


def inherits_from(obj, a_class):
    """ Instance class """

    if type(obj) is bool:
        result = issubclass(type(obj), a_class) and type(obj) is not a_class

    return(result)
