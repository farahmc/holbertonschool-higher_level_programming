#!/usr/bin/python3
"""
Function to read a text file
"""


def read_file(filename=""):
    """
    Read a text file and print to stdout
    """
    with open('my_file_0.txt', encoding="utf-8") as f:
        for line in f:
            print(line, end="")
