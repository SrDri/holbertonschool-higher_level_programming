#!/usr/bin/python3


def uniq_add(my_list=[]):
    resultado = 0
    uniq = set(my_list)

    for i in uniq:
        resultado += i

    return resultado
