#!/usr/bin/python3
"""
class student
"""


class Student:
    """
    Attr:
        first: name
        last: name
        age
    Methods:
        to_json: returns
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs}

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
