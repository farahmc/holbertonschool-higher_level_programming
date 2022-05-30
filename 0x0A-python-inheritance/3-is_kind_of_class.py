#!/usr/bin/python3
"""
Function to check if the object is an instance of, or instance
of a class that inherited from, the specified class
"""


def is_kind_of_class(obj, a_class):
    """
    Return True if object is an instance of a class
    else return False
    """

    if not isinstance(obj, a_class):
        return False

    return True
