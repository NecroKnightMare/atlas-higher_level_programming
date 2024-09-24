#!/usr/bin/python3

from models.rectangle import Rectangle

"""
Module that def Square class that inherits rectangle
"""


class Square(Rectangle):
    """
    square class inherits from rect

    Attributes:
        size: size of square
        x: x value
        y: y value
        id: id is None

    Method:
        string
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        inits Square instance

        Args:
            size: size of sq
            x: int val
            y: int val
            id: id is None
            
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Method:
            __str__: string representation of square
        Returns:
            string
        """
        return f"[Square] ({Square}) {self.x}/{self.y} - {self.width}"
