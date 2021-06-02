#!/usr/bin/python3
""" JSON representation """

import json


def save_to_json_file(my_obj, filename):
    """ Save json write """
    with open(filename, mode="w", encoding="utf-8") as a_file:
        a_file.write(json.dumps(my_obj))
