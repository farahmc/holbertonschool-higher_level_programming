#!/usr/bin/python3
"""
Function that returns JSON representation of a string
"""


def to_json_string(my_obj):
    """
    Return a JSON representation of a string object
    """
    import json

    return json.dumps(my_obj)
