#!/usr/bin/python3
"""
file mod
"""


def append_write(filename="", text=""):
    """
    append file
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
