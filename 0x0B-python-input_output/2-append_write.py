#!/usr/bin/python3
"""
Function to append a string to end of text file
"""


def append_write(filename="", text=""):
    """
    Append a string to end of text file. If the file
    doesn't exist, create it.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        write_file = f.write(text)
        return len(range(write_file))
