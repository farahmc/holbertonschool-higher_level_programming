#!/usr/bin/python3
"""
A class that checks in a given argument is True or False
and returns the inverted result
"""


class MyInt(int):
    """
    A class which returns the inverse of whether a given
    argument is True or False
    """
    def __eq__(self, other):
        """
        Return the inverse of ==
        """
        return self.real != other

    def __ne__(self, other):
        """
        Return the inverse of !=
        """
        return self.real == other
