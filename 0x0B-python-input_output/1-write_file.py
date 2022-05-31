#!/usr/bin/python3
"""
Function to write a string to a text file
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file and return the
    number of characters written (create if file doesn't exist)
    """
    with open(filename, 'w', encoding="utf-8") as f:
        write_file = f.write(text)
        return len(range(write_file))
