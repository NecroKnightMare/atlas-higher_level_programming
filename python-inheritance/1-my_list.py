#!/usr/bin/python3
"""
my list class
"""
class MyList(list):
    """
    prints sorted list
    """
    def print_sorted(self):
        print(sorted(self))
