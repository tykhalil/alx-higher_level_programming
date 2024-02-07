#!/usr/bin/python3

"""
Module with function to create argument list and add to json file
"""


import sys
import json
load = __import__('6-load_from_json_file').load_from_json_file
save = __import__('5-save_to_json_file').save_to_json_file
jsonfile = "add_item.json"
args = sys.argv[1:]
try:
    my_list = load(jsonfile)
except FileNotFoundError:
    save(args, jsonfile)
else:
    my_list.extend(sys.argv[1:])
    save(my_list, jsonfile)
