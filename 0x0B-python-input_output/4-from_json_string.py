#!/usr/bin/python3
"""
Function that returns a Python object from a JSON string
"""


def from_json_string(my_str):
    """
    Return an object represented by a JSON string
    """
    import json

    return json.loads(my_str)
