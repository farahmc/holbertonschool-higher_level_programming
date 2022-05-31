#!/usr/bin/python3
"""
Class student that defines a student
"""


class Student:
    """
    Define a student
    """
    def __init__(self, first_name, last_name, age):
        """
        Instantiate class

        Arguments:
        first_name - first name
        last_name - last name
        age - age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieve a dictionary representation of a student
        """
        return self.__dict__
