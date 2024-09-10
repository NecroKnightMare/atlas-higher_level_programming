#!/usr/bin/python3

"""
Square module with prior size and inc Type error
"""

class Square:

    """
    class size is now an integer, with typerror for >= 0
    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
