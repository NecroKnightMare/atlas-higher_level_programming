#!/usr/bin/python3
"""
module for test to be used on with empty list
"""
def max_integer(list=[]):
    """
    Args:
        list: emp[ty list

    Returns:
        result: of tests
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
