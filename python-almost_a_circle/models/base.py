#!/usr/bin/python3

"""
Parameters:
    id: None
    __nb_objects: 0

Returns:
    id
"""


class Base:
    """
    Base class thatll be the root class for other files
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
