#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

argList = list(sys.argv[1:])

try:
    json_data = load_from_json_file("add_item.json")
except Exception:
    json_data = []

json_data.extend(argList)
save_to_json_file(json_data, "add_item.json")
