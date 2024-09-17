#!/usr/bin/python3
"""
file mod
"""


def read_file(filename=""):
    """
    read file
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read().rstrip())
