#!/usr/bin/python3
"""
Function that adds a new attribute to an object if possible
"""


def add_attribute(ob, att, name):
    """
    Add a new attribute to an object if possible
    """
    if not hasattr(ob, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(ob, att, name)
