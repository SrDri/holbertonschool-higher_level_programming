#!/usr/bin/python3
""" Defines Studentclass """


class Student:
    """ Student class """

    def __init__(self, first_name, last_name, age):
        """ init class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ returns the dictionary description """
        return self.__dict__
