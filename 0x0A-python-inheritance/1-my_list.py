#!/usr/bin/python3

class MyList(list):
    """
    Class that inherits from list
    """

    def print_sorted(self):
        """
        Print a sorted (ascending) list
        """
        print(sorted(self))
