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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Method to share data representation

        Args:
            list_dictionaries

        Return:
            json rep of arg
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
