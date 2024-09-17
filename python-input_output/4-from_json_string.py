#!/usr/bin/python3
"""
file json mod
"""


def from_json_string(my_str):
    """
    returns str into json obj
    """
    import json
    return json.loads(my_str)
