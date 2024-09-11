#!/usr/bin/python3

"""
add two int or floats
"""

def add_integer(a, b=98):
    """
    Arg:
        a: firt number
        b: second number

    Returns:
        sum of a and b

    Raises:
        TE if not integers
        OverflowError: float overflow
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float) and (a > 1e308 or a < -1e308):
        raise OverflowError("a is too large")
    if isinstance(b, float) and (b > 1e308 or b < -1e308):
        raise OverflowError("b is too large")

    a = int(a)
    b = int(b)

    return a + b
