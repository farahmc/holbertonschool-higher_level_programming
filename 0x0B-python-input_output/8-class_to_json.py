#!/usr/bin/python3
"""
Function returning dictionary description
with simple data structure for JSON serialization of an object
"""


def class_to_json(obj):
    """
    Return a dictionary description with simple data structure
    for JSON serialization of an object
    """
    return obj.__dict__
