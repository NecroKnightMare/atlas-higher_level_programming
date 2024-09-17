#!/usr/bin/python3
"""
file json mod
"""


def save_to_json_file(my_obj, filename):
    """
    save obj to file
    """
    import json
    with open(filename, "w") as file:
        json.dump(my_obj, filename)
