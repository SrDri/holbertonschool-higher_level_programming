#!/usr/bin/python3
import json
""" Base class """


class Base:
    """ The Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor Base class """
        if id is None:
            Base.__nb_objects += 1
            id = self.__nb_objects

        self.id = id

    def to_json_string(list_dictionaries):
        """ return the JSON string representation"""
        if list_dictionaries == None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)
