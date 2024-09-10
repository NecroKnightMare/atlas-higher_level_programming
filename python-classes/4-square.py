#!/usr/bin/python3

"""
Square mmodule

"""

class Square:
    """
    Attributes:
        _size (int): size of square

    Methods:
        size: gets or sets size of square
        area: calcs area of square
"""
    def __init__(self, size=0):
        self._size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        return self._size ** 2
