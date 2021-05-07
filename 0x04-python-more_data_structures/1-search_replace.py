#!/usr/bin/python3


def search_replace(my_list, search, replace):
    count = my_list.count(search)
    new = my_list.copy()

    if count != 0:
        for i in range(0, count):
            new[new.index(search)] = replace

    return new
