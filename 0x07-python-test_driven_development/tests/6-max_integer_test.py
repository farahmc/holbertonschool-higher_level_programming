#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Unit Testing for finding max integer in a list
    """
    def test_ordered_positive(self):
        """ Test a list of ordered integers """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_positive(self):
        """ Test a list of unordered integers """
        self.assertEqual(max_integer([8, 15, 36, 2]), 36)

    def test_ordered_negative(self):
        """ Test a list of ordered negative integers """
        self.assertEqual(max_integer([-12, -8, -6, -2]), -2)

    def test_unordered_negative(self):
        """ Test a list of unordered negative integers """
        self.assertEqual(max_integer([-31, -1, -12, -15]), -1)

    def test_identical(self):
        """ Test a list of identical values """
        self.assertEqual(max_integer([31, 31, 31, 31]), 31)

    def test_unordered_float(self):
        """ Test a list of floats """
        self.assertEqual(max_integer([10.4, 1.854, 3.6, 5.88]), 10.4)

    def test_unordered_negativefloat(self):
        """ Test a list of unordered negative floats """
        self.assertEqual(max_integer([-31.25, -234.5, -31.15, -55.2]), -31.15)

    def test_mixed_numbers(self):
        """ Test a list of unordered floats and integers """
        self.assertEqual(max_integer([-31, 12.3, 12, -15.34, 7]), 12.3)

    def test_one(self):
        """ Test a list of one element """
        self.assertEqual(max_integer([2]), 2)

    def test_string(self):
        """ Test a string """
        self.assertEqual(max_integer("Hello"), "o")

    def test_string_list(self):
        """ Test a list of strings """
        self.assertEqual(max_integer(["hello", "world", "can", "you", "see"]), "you")

    def test_tuple(self):
        """ Test a tuple """
        self.assertEqual(max_integer((5, 10, 3, 7)), 10)

    def test_inf(self):
        """ Test a list with infinity """
        self.assertEqual(max_integer([float('inf'), 3, 1000, 68]), float('inf'))

    def test_empty(self):
        """ Test an empty list """
        self.assertEqual(max_integer([]), None)

    def test_list_mixed(self):
        """ Raise an error when list is mixed """
        with self.assertRaises(TypeError):
            max_integer([-31, "hello", 12, 15])

    def test_true(self):
        """ Raise an error when True is passed """
        with self.assertRaises(TypeError):
            max_integer(True)

if __name__ == '__main__':
    unittest.main()
