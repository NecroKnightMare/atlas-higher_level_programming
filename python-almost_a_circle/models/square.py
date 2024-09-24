#!/usr/bin/python3

"""
Module that def Square class that inherits rectangle
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    square class inherits from rect

    Attributes:
        size: size of square
        x: x value
        y: y value
        id: id is None
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

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        super().integer_validator("width", value)
        self.width = value
        self.height = value


    def __str__(self):
        """
        Method:
            __str__: string representation of square
        Returns:
            string
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
