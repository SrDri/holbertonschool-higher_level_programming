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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ return the JSON string representation"""
        if list_dictionaries == None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file"""
        contenido = []

        if list_objs is not None:
            contenido = []
            for i in list_objs:
                contenido.append(cls.to_dictionary(i))

        with open(cls.__name__ + ".json", 'w') as out_file:
            out_file.write(cls.to_json_string(contenido))
