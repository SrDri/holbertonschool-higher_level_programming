#!/usr/bin/python3
""" Defines Studentclass """


class Student:
    """ Student class """

    def __init__(self, first_name, last_name, age):
        """ init class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ returns the dictionary description """
        if attrs is None:
            return self.__dict__
        else:
            aux = {}

            for key in attrs:
                if key in self.__dict__:
                    aux[key] = self.__dict__[key]

            return aux

    def reload_from_json(self, json):
        for key, value in json.items():
            if key is self.__dict__:
                self.__dict__[key] = value
                    