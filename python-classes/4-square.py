#!/usr/bin/python3

"""
Square mmodule
"""

class Square:

    """
    updaate attribute with value
    """
    def __init__(self, size=0):
        self.__size = size

    def size(self):
        return self.__size

    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size
