#!/usr/bin/python3
"""Function to print first and last name"""

def is_number(string):
    """
    Compares each character in string to see if there is a number
    """
    isdigit = str.isdigit
    return any(map(isdigit, string))

def say_my_name(first_name, last_name=""):
    """
    Print first and last name

    Arguments:
    first_name: First name (must be passed)
    last_name: Last name (optional, initialised as an empty string)
    """
    if not isinstance(first_name, str) or len(first_name) < 1:
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if is_number(first_name) is True or is_number(last_name) is True:
        raise ValueError("first_name and last_name cannot contain numbers")
    print(f"My name is {first_name} {last_name}")
