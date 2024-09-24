#!/usr/bin/python3

from models.rectangle import Rectangle

"""
Square class that imports rectangle
"""


class Square(Rectangle):
    """
    Attributes:
        size
        x
        y
        id

    Method:
        string
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns:
            string
        """
        return f"[Square] ({Square}) {self.x}/{self.y} - {self.width}"
