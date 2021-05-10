#!/usr/bin/python3


def roman_to_int(roman_string):
    if roman_string and isinstance(roman_string, str) == True:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50,
                 "C": 100, "D": 500, "M": 1000}
        prev = 0
        resultado = 0

        for c in roman_string:
            if prev < roman[c]:
                resultado = resultado - prev * 2

            prev = roman[c]
            resultado = resultado + roman[c]

        return resultado
    else:
        return 0
