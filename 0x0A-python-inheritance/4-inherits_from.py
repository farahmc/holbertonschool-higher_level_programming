#!/usr/bin/python3
"""
Function that checks if an object is an instance of a class
that inherited directly or indirectly from the specified class
"""

def inherits_from(obj, a_class):
    """
    Return True if object is an instance of a class that
    inherited from the specified class
    Otherwise return False
    """
    if isinstance(obj, a_class) is True and type(obj) != a_class:
        return True

    return False
