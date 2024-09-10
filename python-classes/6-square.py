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
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        x, y = value
        if not isinstance(x, int) or not isinstance(y, int):
            rasie TypeError("position must be a tuple of 2 positive integers")
        if x < 0 or y < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value


    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
            return

        num_lines = self.__position[1] + self.__size

        print(" " * self.__position[0], ends="")

        for _ in range(num_lines):
            print("#" * self.__size)
