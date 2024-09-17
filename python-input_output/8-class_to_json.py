#!/usr/bin/python3
"""
json mod
"""
import json


def class_to_json(obj):
    """
    returns obj dict
    """
    return obj.__dict__
