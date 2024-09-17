#!/usr/bin/python3
"""
file json mod
"""

import json


def save_to_json_file(my_obj, filename):
    """
    save obj to file
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
