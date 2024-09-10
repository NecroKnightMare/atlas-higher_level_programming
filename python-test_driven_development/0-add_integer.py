#!/usr/bin/python3

def add_integers(a, b=98):
    """
    adds integers

    Args:
        a: int float 98
        b: int float 98
    

    Returns:
        int: sum of a and b

    Raises:
        TypeError for non integer
   """

    a_int = int(a)
    b_int = int(b)

    if not isinstance(a_int, (int, float)) or not isinstance(b_int(int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    result = a_int + b_int

    return = result
