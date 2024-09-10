#!/usr/bin/python3
"""
prints "my name is [first][last]
"""

def say_my_name(first_name, last_name=""):
    """
    Parameters:
        first_name: first name
        last_name: last name

    Raises:
        TypeError: if not a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
