#!/usr/bin/python3
""" JSON representation """
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


file_name = "add_item.json"

try:
    cargar = load_from_json_file(file_name)
    save_to_json_file(cargar + sys.argv[1:], file_name)
except:
    save_to_json_file([] + sys.argv[1:], file_name)
