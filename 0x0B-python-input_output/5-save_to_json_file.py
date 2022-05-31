#!/usr/bin/python3
"""
Function to write an object to a text file using a JSON
representation
"""


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using a JSON representation
    """
    import json

    with open(filename, 'w', encoding="utf-8") as fp:
        write_file = json.dump(my_obj, fp)
