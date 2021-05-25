#!/usr/bin/python3
import sys
sys.path.append('../')

matrix_divided = __import__('2-matrix_divided').matrix_divided

# 1. Matrix divided by 1
print(matrix_divided([[1, 2], [3, 4]], 1))
# [[1.0, 2.0], [3.0, 4.0]]

# 2. Matrix divided by 0
# print(matrix_divided([[1, 2], [3, 4]], 0))
# Traceback (most recent call last):
# ZeroDivisionError: division by zero

# 3. Matrix divided by string
# print(matrix_divided([[0, 0], [0, 0]], 'Hola'))
# Traceback (most recent call last):
# TypeError: div must be a number

# 4. Matrix error size
# print(matrix_divided([[1, 2], [3, 4], [10]], 2))
# Traceback (most recent call last):
# TypeError: Each row of the matrix must have the same size

# 5. No div in arguments
# print(matrix_divided([[1, 2, 3], [4, 5, 6]]))
# Traceback (most recent call last):
# TypeError: matrix_divided() missing 1 required positional argument: 'div'

# 6. String in matrix
# print(matrix_divided([[1, 2, 3], [4, 'cinco', 'seis']], 2))
# Traceback (most recent call last):
# TypeError: matrix must be a matrix (list of lists) of integers/floats

# 7. No arguments
# print(matrix_divided())
# Traceback (most recent call last):
# TypeError: matrix_divided() missing 2 required positional arguments: 'matrix' and 'div'
