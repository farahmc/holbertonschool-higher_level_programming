#!/usr/bin/python3
"""
Function to check if object is an exact instance of the
specified class
"""


def is_same_class(obj, a_class):
    """
    Return True if object is exactly an instance
    of the specified class, else return False
    """
    if type(obj) != a_class:
        return False

    return True
