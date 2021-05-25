#!/usr/bin/python3
import sys
sys.path.append('../')

text_indentation = __import__('5-text_indentation').text_indentation

# 2. print mi name
# print(text_indentation("Hola. Mi. Nombre. es. Juan Jose        .         "))
# Hola.
# <BLANKLINE>
# Mi.
# <BLANKLINE>
# Nombre.
# <BLANKLINE>
# es.
# <BLANKLINE>
# Juan Jose        .
# <BLANKLINE>

# 3. Print test spaces
# print(text_indentation("   This is. a test."))
# This is .
# <BLANKLINE>
# a test.
# <BLANKLINE>

# 4. Print int
# print(text_indentation("1"))
# 1

# 5. Int in argument
# print(text_indentation(1))
# Traceback (most recent call last):
# TypeError: text must be a string

# 6. Test quotes
print(text_indentation(""""""))
# <BLANKLINE>

# 7. test \n
print(text_indentation("Hello.\nWorld"))
# Hello.
# <BLANKLINE>
# <BLANKLINE>
# World
