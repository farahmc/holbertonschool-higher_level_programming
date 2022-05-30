#!/usr/bin/python3
"""
Defines a class called MyList
"""


class MyList(list):
    """
    Class that inherits from list

    Attributes:
    print_sorted - prints sorted list
    """

    def print_sorted(self):
        """
        Print a sorted (ascending) list
        """
        print(sorted(self))
