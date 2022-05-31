#!/usr/bin/python3
"""
Function that creates an object from a JSON file
"""


def load_from_json_file(filename):
    """
    Create an object from a JSON file

    Arguments:
    filename - the JSON file to read

    Return:
    JSON object
    """
    import json

    with open(filename, encoding="utf-8") as fp:
        return json.load(fp)
