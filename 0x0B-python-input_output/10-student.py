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
        first_name - first name of student
        last_name - last name of student
        age - age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance
        If attrs is a list of strings, only attribute names contained in this
        list must be retrieved
        """
        if type(attrs) == list and all(type(el) == str for el in attrs):
            new_dict = {key: getattr(self, key) for key in attrs
                        if hasattr(self, key)}
            return new_dict
        return self.__dict__
