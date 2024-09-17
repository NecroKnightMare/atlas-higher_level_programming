#!/usr/bin/python3
"""
inheritance
"""


def inherits_from(obj, a_class):
    """
    if inherited directly or indirectly will return as such
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
