#!/usr/bin/python3
"""
ret a list object
"""
def lookup(obj):
    try:
        return sorted(dir(obj))
    except Exception as e:
        print(f"Error occurerd: {str(e)}")
        return[]
