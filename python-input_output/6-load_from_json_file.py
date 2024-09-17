#!/usr/bin/python3
import json
"""
json file mod
"""


def load_from_json_file(filename):
    """
    load from json
    """
    with open(filename, "r") as file:
        return json.load(filename)
