#!/usr/bin/python3
import sys
sys.path.append('../')

print_square = __import__('4-print_square').print_square

# 2. print square
print(print_square(4))
####
####
####
####

# 3. negative square
# print(print_square(-5))
# Traceback (most recent call last):
# ValueError: size must be >= 0

# 4. String in argument
# print(print_square("hola"))
# Traceback (most recent call last):
# TypeError: size must be an integer

# 5. Zero square
print(print_square(0))
#

# 6. No arguments
# print(print_square())
# Traceback (most recent call last):
# TypeError: print_square() missing 1 required positional argument: 'size'

# 7. Float Argument
print(print_square(3.5))
# Traceback (most recent call last):
# TypeError: size must be an integer
