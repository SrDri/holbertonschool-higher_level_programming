#!/usr/bin/python3
""" JSON representation """

import json


def load_from_json_file(filename):
    """ json load """
    with open(filename, mode="r", encoding="utf-8") as a_file:
        return json.load(a_file)
