#!/usr/bin/python3
"""
file mod
"""


def write_file(filename="", text=""):
    """
    write into file
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
