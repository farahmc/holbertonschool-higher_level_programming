#!/usr/bin/python3
"""
Contains tests for Rectangle class - Task 2
Focus is on:
- setting private instance attributes in the constructor using
  getters and setters
- calling super()__init__() to set public instance id attribute
"""

import unittest
import inspect
import pycodestyle

from models.base import Base
from models import rectangle
Rectangle = rectangle.Rectangle


class TestRectangleDocs(unittest.TestCase):
    """Tests for documentation of class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.rect_funcs = inspect.getmembers(Rectangle, inspect.isfunction)

    def test_conformance_class(self):
        """Test that we conform to Pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_conformance_test(self):
        """Test that we conform to Pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstr(self):
        """Tests for docstring"""
        self.assertTrue(len(rectangle.__doc__) >= 1)

    def test_class_docstr(self):
        """Tests for docstring"""
        self.assertTrue(len(Rectangle.__doc__) >= 1)

    def test_func_docstr(self):
        """Tests for docstrings in all functions"""
        for func in self.rect_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestRectangle(unittest.TestCase):
    """ Tests functionality of class"""

    def test_properties(self):
        """Tests all setters and getters"""
        Base._Base__nb_objects = 0
        r_1 = Rectangle(1, 1)
        self.assertEqual(r_1.width, 1)
        self.assertEqual(r_1.height, 1)
        self.assertEqual(r_1.x, 0)
        self.assertEqual(r_1.y, 0)

        r_1.x = 10
        r_1.y = 10
        self.assertEqual(r_1.x, 10)
        self.assertEqual(r_1.y, 10)

    """ Tests functionality of super()__init__() call"""

    def test_id_none(self):
        """Tests id not passed in"""
        Base.__nb_object = 0
        r_2 = Rectangle(1, 1)
        self.assertEqual(r_2.id, 1)

    def test_id_assigned(self):
        """Tests id passed in"""
        r_3 = Rectangle(1, 1, 1, 1, 88)
        self.assertEqual(r_3.id, 88)

    def test_nb_object_increment(self):
        """Tests private class attribute incrementation"""
        r_4 = Rectangle(1, 1)
        self.assertEqual(r_4.id, 2)

    """Tests number of arguments passed in"""
    def test_too_many_args(self):
        """Tests entering too many args to instantiate object"""
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, 4, 5, 6)

    def test_too_few_args(self):
        """Tests entering too few args to instantiate object"""
        with self.assertRaises(TypeError):
            r = Rectangle()


class TestRectangle_w(unittest.TestCase):
    """ Unit tests for Rectangle width attribute """

    def test_neg_w(self):
        """ Test negative number """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-3, 5)

    def test_zero_w(self):
        """ Test 0 """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 5)

    def test_float_w(self):
        """ Test float """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(1.2, 5)

    def test_tuple_w(self):
        """ Test a tuple """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((3, 2), 5)

    def test_infinity_w(self):
        """ Test infinity """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 3)

    def test_nan_w(self):
        """ Test NaN """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 3)

    def test_string_w(self):
        """ Test string """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("hello", 5)

    def test_list_w(self):
        """ Test list """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2], 5)

    def test_dict_w(self):
        """ Test dictionary """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"1": 1, "2": 2}, 5)


class TestRectangle_h(unittest.TestCase):
    """ Unit tests for Rectangle height attribute """

    def test_neg_h(self):
        """ Test negative number """
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(3, -5)

    def test_zero_h(self):
        """ Test 0 """
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(5, 0)

    def test_float_h(self):
        """ Test float """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 5.1)

    def test_tuple_h(self):
        """ Test a tuple """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, (3, 2))

    def test_infinity_h(self):
        """ Test infinity """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, float('inf'))

    def test_nan_h(self):
        """ Test NaN """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, float('nan'))

    def test_string_h(self):
        """ Test string """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, "hello")

    def test_list_h(self):
        """ Test list """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, [1, 2])

    def test_dict_h(self):
        """ Test dictionary """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, {"1": 1, "2": 2})


class TestRectangle_x(unittest.TestCase):
    """ Unit tests for Rectangle x attribute """

    def test_neg_x(self):
        """ Test negative number """
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(3, 5, -2)

    def test_float_x(self):
        """ Test float """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 3, 5.1)

    def test_tuple_x(self):
        """ Test a tuple """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 4, (3, 2))

    def test_infinity_x(self):
        """ Test infinity """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 4, float('inf'))

    def test_nan_x(self):
        """ Test NaN """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 4, float('nan'))

    def test_string_x(self):
        """ Test string """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 4, "hello")

    def test_list_x(self):
        """ Test list """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 4, [1, 2])

    def test_dict_x(self):
        """ Test dictionary """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 4, {"1": 1, "2": 2})


class TestRectangle_y(unittest.TestCase):
    """ Unit tests for Rectangle y attribute """

    def test_neg_y(self):
        """ Test negative number """
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(3, 5, 6, -2)

    def test_float_y(self):
        """ Test float """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 3, 4, 5.1)

    def test_tuple_y(self):
        """ Test a tuple """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 4, 6, (3, 2))

    def test_infinity_y(self):
        """ Test infinity """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 4, 5, float('inf'))

    def test_nan_y(self):
        """ Test NaN """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 4, 5, float('nan'))

    def test_string_y(self):
        """ Test string """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 4, 3, "hello")

    def test_list_y(self):
        """ Test list """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 4, 3, [1, 2])

    def test_dict_y(self):
        """ Test dictionary """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 4, 3, {"1": 1, "2": 2})


class TestRectangle_area(unittest.TestCase):
    """ Unit tests for area method """

    def test_area_(self):
        """ Test area """
        rec = Rectangle(5, 20, 1, 1, 0)
        self.assertEqual(100, rec.area())

    def test_area_large(self):
        """ Test large area """
        rec = Rectangle(35468786453513213654654, 3165488674541351, 1, 1, 0)
        self.assertEqual(112276041818321768348545216113956597554, rec.area())

    def test_area_change(self):
        """ Test changed attributes """
        rec = Rectangle(5, 20, 1, 1, 0)
        rec.width = 2
        rec.height = 4
        self.assertEqual(8, rec.area())


class TestRectangle_update(unittest.TestCase):
    """ Unit tests for update method """

    def test_update_id(self):
        """ Test update 1st argument """
        rec = Rectangle(1, 2, 3, 4, 5)
        rec.update(10)
        self.assertEqual("[Rectangle] (10) 3/4 - 1/2", str(rec))

    def test_update_w(self):
        """ Test update 2nd argument """
        rec = Rectangle(1, 2, 3, 4, 5)
        rec.update(10, 9)
        self.assertEqual("[Rectangle] (10) 3/4 - 9/2", str(rec))

    def test_update_h(self):
        """ Test update 3rd argument """
        rec = Rectangle(1, 2, 3, 4, 5)
        rec.update(10, 9, 8)
        self.assertEqual("[Rectangle] (10) 3/4 - 9/8", str(rec))

    def test_update_x(self):
        """ Test update 4th argument """
        rec = Rectangle(1, 2, 3, 4, 5)
        rec.update(10, 9, 8, 7)
        self.assertEqual("[Rectangle] (10) 7/4 - 9/8", str(rec))

    def test_update_y(self):
        """ Test update 5th argument """
        rec = Rectangle(1, 2, 3, 4, 5)
        rec.update(10, 9, 8, 7, 6)
        self.assertEqual("[Rectangle] (10) 7/6 - 9/8", str(rec))

    def test_update_again(self):
        """ Test update twice """
        rec = Rectangle(1, 2, 3, 4, 5)
        rec.update(10, 9, 8, 7, 6)
        rec.update(11, 12, 13, 14, 15)
        self.assertEqual("[Rectangle] (11) 14/15 - 12/13", str(rec))

    def test_update_kwargs(self):
        """ Test updating with key, values """
        rec = Rectangle(1, 2, 3, 4, 5)
        rec.update(y=10, id=9, height=8, width=7, x=6)
        self.assertEqual("[Rectangle] (9) 6/10 - 7/8", str(rec))

    def test_update_None(self):
        """ Test None in id """
        rec = Rectangle(1, 2, 3, 4, 5)
        rec.update(None, 9, 8, 7, 6)
        self.assertEqual("[Rectangle] (None) 7/6 - 9/8", str(rec))
