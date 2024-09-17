#!/usr/bin/python3
"""
json file mod
"""


import json
def load_from_json_file(filename):
    """
    load from json
    """
    with open(filename, "r") as file:
        return json.load(filename)
