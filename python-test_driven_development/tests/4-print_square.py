#!/usr/bin/python3
"""
prints a square using #
"""
def print_square(size):
    """
    Args:
        size: length of square

    Raises:
        TypeError: if size not an integer
        ValueError: if size < 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
