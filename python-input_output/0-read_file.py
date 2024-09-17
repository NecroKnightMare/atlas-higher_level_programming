#!/usr/bin/python3
"""
file mod
"""


def read_file(filename=""):
    """
    read file
    """
    try:
        with open(filename, 'r', encoding="utf-8") as file:
            print(file.read().strip())

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
