#!/usr/bin/python3
import sys
sys.path.append('../')

add_integer = __import__('0-add_integer').add_integer

# 1. Suma dos enteros
print(add_integer(2, 2))
# 4

# 2. suma de dos float
print(add_integer(5.1, 5.2))
# 10

# 3. suma de dos int negativos
print(add_integer(-5, -5))
# -10

# 4. suma de un string y un int: TypeError(a)
# print(add_integer("5", 5))
# TypeError: a must be an integer

# 5. suma de un string y un int: TypeError(b)
# print(add_integer(-5, "hola"))
# TypeError: b must be an integer

# 6. suma ridiculously large:
print(add_integer(99, 1e100))
# 10000000000000000159028911097599180468360808563945281389781327557747838772170381060813469985856815203

# 7. No argument
# print(add_integer())
# TypeError: add_integer() missing 1 required positional argument: 'a'

# 8. ValueError for int
# print(add_integer(int('hola')))
# ValueError: invalid literal for int() with base 10: 'hola'

# 9. Work with only one argument
# print(add_integer(102))
# 200

print("------------")

print(add_integer(float('inf')))
