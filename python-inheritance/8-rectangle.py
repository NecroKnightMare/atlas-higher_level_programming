#!/usr/bin/python3
"""
class basegeometry
"""


class BaseGeometry:
    """
    paramter:
        area: create area
        integer_validator: creates value

    Raise:
        Exception
        TyperError
        ValueError
    """
    def area(self):
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
"""
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
        super().self.integer_validator("width", width)
        super().self.integer_validator("height", height)
        self.__width = width
        self.__height = height
    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
