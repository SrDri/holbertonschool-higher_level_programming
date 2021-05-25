#!/usr/bin/python3
import sys
sys.path.append('../')

say_my_name = __import__('3-say_my_name').say_my_name

# 1. normal function
print(say_my_name("Juan", "Carabali"))
# My name is Juan Carabali

# 2. int in first argument
# print(say_my_name(404, "Juan"))
# Traceback (most recent call last):
# TypeError: first_name must be a string

# 3. int in second argument
# print(say_my_name("Juan", 404))
# Traceback (most recent call last):
# TypeError: last_name must be a string

# 4. No arguments
# print(say_my_name())
# Traceback (most recent call last):
# TypeError: say_my_name() missing 1 required positional argument: 'first_name'

# 5. Int in arguments
# print(say_my_name(2 + 2, 50))
# Traceback (most recent call last):
# TypeError: first_name must be a string
