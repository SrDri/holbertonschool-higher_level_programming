#!/usr/bin/python3
""" `is_same_class` function """


def is_same_class(obj, a_class):
    """ Instance class """

    resultado = type(obj) is a_class
    return(resultado)
