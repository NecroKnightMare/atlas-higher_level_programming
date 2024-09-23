#!/usr/bin/python3
"""
Rectangle class thatll pull from Base class
and gives an area
"""
from models.base import Base


class Rectangle(Base):
    """
    gets area of a rectangle

    Attributes:
        width
        height
        x
        y
        area

    Returns:
        rectangle int: values and area of rectangle
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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        gets area of a rectangle

        Attributes:
            width
            height
            x
            y
            area

        Returns:
            rectangle int: values and area of rectangle
        """
        return self.width * self.height

    def display(self):
        """
        print # repr rectangle
        """
        for _ in range(self.height):
            print("#" * self.width)
