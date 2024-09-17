#!/usr/bin/python3
from models.base_geometry import BaseGeometry
"""
class basegeometry
class rectangle
"""


class Rectangle(BaseGeometry):
    """
    initiation of
    Parameters:
        width
        height
    """
    def __init__(self, width, height):
        self.integer__validator("width", width)
        self.integer__validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        return "[Rectangle] {}/{}.format(self.__width, self.__height)"

    def area(self):
        return self.__width * self.__height
