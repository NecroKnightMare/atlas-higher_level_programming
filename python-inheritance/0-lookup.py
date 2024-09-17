#!/usr/bin/python3
"""
function  to print an obj list
"""


def lookup(obj):
    """
    returns a list object
    """
    try:
        return sorted(dir(obj))
    except Exception as e:
        print(f"Error occurerd: {str(e)}")
        return[]
