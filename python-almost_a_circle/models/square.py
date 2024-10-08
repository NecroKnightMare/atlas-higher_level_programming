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
        self.width = value
        self.height = value

    def integer_validator(self, name, value):
        """
        error handle on value
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be greater than 0")

    def update(self, *args, **kwargs):
        """
        Method to assign arguments to attributes
        """

        if args:
            attributes = ['id', 'size', 'x', 'y']
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)

        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Method to return square as a dictionary
        """

        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }

    def __str__(self):
        """
        Method:
            __str__: string representation of square
        Returns:
            string
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
