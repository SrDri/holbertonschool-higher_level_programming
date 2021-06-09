#!/usr/bin/python3
"""Base class"""
import json


class Base:
    """ The Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor Base class """
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ return the JSON string representation"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file"""
        contenido = []

        if list_objs is not None:
            contenido = []
            for i in list_objs:
                contenido.append(cls.to_dictionary(i))

        with open(cls.__name__ + ".json", 'w', encoding="utf-8") as out_file:
            out_file.write(cls.to_json_string(contenido))

    @staticmethod
    def from_json_string(json_string):
        """ return list JSON string representation"""
        if json_string is None or len(json_string) == 0:
            return "[]"

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ return an all attributes """
        if cls.__name__ == "Rectangle":
            aux = cls(1, 1)
        elif cls.__name__ == "Square":
            aux = cls(1)

        # pass the dictionary as a double pointer
        aux.update(**dictionary)

        return aux

    @classmethod
    def load_from_file(cls):
        """ Return list of instances """
        try:
            with open(cls.__name__ + ".json", "r") as out_file:
                contenido = cls.from_json_string(out_file.read())

                aux = []
                for elem in contenido:
                    aux.append(cls.create(**elem))

                return aux

        except FileNotFoundError:
            return []
