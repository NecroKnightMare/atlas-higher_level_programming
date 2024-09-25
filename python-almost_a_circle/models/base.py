#!/usr/bin/python3

"""
Parameters:
    id: None
    __nb_objects: 0

Returns:
    id
"""
import json
import os


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

    @staticmethod
    def from_json_string(json_string):
        """
        S Method ret list of json string representation of json_string
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Method write to json string representing of list_objs to a file

        Args:
            list_objs
        """
        filename = f"{cls.__name__}.json"
        with open(filename, 'w') as file:
            if list_objs is None:
                file.write(cls.to_json_string([]))
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dicts))

    @classmethod
    def load_from_file(cls):
        """
        class method that ret a list of instances
        """
        filename = f"{cls.__name__}.json"
        if not os.path.exists(filename):
            return []

        with open(filename, 'r') as file:
            json_string = file.read()
            list_dicts = cls.from_json_string(json_string)
            return [cls.create(**d) for d in list_dicts]
    
    @classmethod
    def create(cls, **dictionary):
        """
        c method creates dummy instance
        with all atts set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = None

        if dummy:
            dummy.update(**dictionary)
        return dummy
