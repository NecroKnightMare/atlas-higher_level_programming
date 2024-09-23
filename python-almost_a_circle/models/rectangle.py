#!/usr/bin/python3
"""
Rectangle class thatll pull from Base class
"""
from models.base import Base


class Rectangle(Base):
    """
    Attributes:
        width
        height
        x
        y

    Returns:
        rectangle values

    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        if value is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        if value is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value
        if x < 0:
            raise ValueError("x must be >= 0")
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
        if y < 0:
            raise ValueError("y must be >= 0")
