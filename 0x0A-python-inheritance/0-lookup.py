#!/usr/bin/python3
"""
Function that returns list of available attributes
and methods of an object
"""


def lookup(obj):
    """
    Return the list of available attributes
    and methods of an object in a list

    Arguments:
    obj - the object to assess
    """
    return(list(dir(obj)))
