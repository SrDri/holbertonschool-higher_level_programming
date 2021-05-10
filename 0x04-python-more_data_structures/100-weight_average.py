#!/usr/bin/python3


def weight_average(my_list=[]):

    if len(my_list) == 0:
        return 0

    sum_of_mul = 0
    sum_of_sec = 0

    for tp in my_list:
        sum_of_mul = sum_of_mul + tp[0] * tp[1]
        sum_of_sec = sum_of_sec + tp[1]

    return sum_of_mul / sum_of_sec
