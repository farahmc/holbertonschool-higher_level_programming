#!/usr/bin/python3
""" Contains tests for class Square"""


import unittest
import inspect
import pycodestyle

from models.base import Base
from models import square
Square = square.Square


class TestSquareDocs(unittest.TestCase):
    """ Tests for documentation of class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.square_funcs = inspect.getmembers(Square, inspect.isfunction)

    def test_conformance_class(self):
        """Test that we conform to Pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_conformance_test(self):
        """Test that we conform to Pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstr(self):
        """ Tests for docstring"""
        self.assertTrue(len(square.__doc__) >= 1)

    def test_class_docstr(self):
        """ Tests for docstring"""
        self.assertTrue(len(Square.__doc__) >= 1)

    def test_func_docstr(self):
        """Tests for docstrings in all functions"""
        for func in self.square_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestSquare(unittest.TestCase):
    """ Test for functionality of class"""

    @classmethod
    def setUpClass(cls):
        """set up the tests"""
        Base._Base__nb_objects = 0
        cls.s1 = Square(1)
        cls.s2 = Square(2, 3)
        cls.s3 = Square(4, 5, 6)
        cls.s4 = Square(7, 8, 9, 10)

    def test_str(self):
        """Test the __str__ method"""
        self.assertEqual(str(self.s1), "[Square] (1) 0/0 - 1")
        self.assertEqual(str(self.s2), "[Square] (2) 3/0 - 2")

    def test_id(self):
        """test if id is not given"""
        self.assertEqual(self.s1.id, 1)
        self.assertEqual(self.s2.id, 2)
        self.assertEqual(self.s3.id, 3)
        self.assertEqual(self.s4.id, 10)

    def test_size(self):
        """Test for functioning size"""
        self.assertEqual(self.s1.size, 1)
        self.assertEqual(self.s2.size, 2)
        self.assertEqual(self.s3.size, 4)
        self.assertEqual(self.s4.size, 7)

    def test_width(self):
        self.assertEqual(self.s1.width, 1)
        self.assertEqual(self.s2.width, 2)
        self.assertEqual(self.s3.width, 4)
        self.assertEqual(self.s4.width, 7)

    def test_height(self):
        """Test for functioning height"""
        self.assertEqual(self.s1.height, 1)
        self.assertEqual(self.s2.height, 2)
        self.assertEqual(self.s3.height, 4)
        self.assertEqual(self.s4.height, 7)

    def test_x(self):
        """Test for functioning x"""
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s2.x, 3)
        self.assertEqual(self.s3.x, 5)
        self.assertEqual(self.s4.x, 8)

    def test_y(self):
        """Test for functioning y"""
        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s2.y, 0)
        self.assertEqual(self.s3.y, 6)
        self.assertEqual(self.s4.y, 9)

    def test_noArgs(self):
        """Test with no args"""
        with self.assertRaises(TypeError):
            s = Square()

    def test_toomanyArgs(self):
        """Test with too many args"""
        with self.assertRaises(TypeError):
            r = Square(1, 2, 3, 4, 5, 6)

    def test_sizeWrongData(self):
        """Test non-ints for size"""
        with self.assertRaises(TypeError):
            s = Square("hello")
        with self.assertRaises(TypeError):
            s = Square(True)

    def test_xWrongData(self):
        """Test non-ints for x"""
        with self.assertRaises(TypeError):
            s = Square(1, "hello")
        with self.assertRaises(TypeError):
            s = Square(1, True)

    def test_yWrongData(self):
        """Test non-ints for y"""
        with self.assertRaises(TypeError):
            s = Square(1, 1, "hello")
        with self.assertRaises(TypeError):
            s = Square(1, 1, True)

    def test_size_neg(self):
        """Test ints <= 0 for size"""
        with self.assertRaises(ValueError):
            s = Square(-1)
        with self.assertRaises(ValueError):
            s = Square(0)

    def test_x_neg(self):
        """Test ints < 0 for x"""
        with self.assertRaises(ValueError):
            s = Square(1, -1)

    def test_y_neg(self):
        """Test ints <= 0 for y"""
        with self.assertRaises(ValueError):
            s = Square(1, 1, -1)

    def test_area(self):
        """test area"""
        self.assertEqual(self.s1.area(), 1)
        self.assertEqual(self.s2.area(), 4)
        self.assertEqual(self.s3.area(), 16)
        self.assertEqual(self.s4.area(), 49)

    def test_area_args(self):
        """Test too many args for area()"""
        with self.assertRaises(TypeError):
            r = self.s3.area(1)

    def test_issubclass(self):
        """test to check sub class"""
        self.assertTrue(issubclass(Square, Base), True)

    def test_tooManyArgs(self):
        """tests for too many arguments"""
        with self.assertRaises(TypeError):
            s = Square(1, 2, 3, 4, 5, 6, 7, 8, 9)

    def test_setter(self):
        """tests setter"""
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.size, 1)
        s.size = 100
        self.assertEqual(s.size, 100)

    def test_update_number_of_args(self):
        """ Test update method with number of arguments passed in"""
        sq = Square(5, 5, 5, 5)
        sq.update()
        self.assertEqual(str(sq), "[Square] (5) 5/5 - 5")
        sq1 = Square(11)
        sq1.update(1, 1, 1, 1, 1)
        self.assertEqual(str(sq1), "[Square] (1) 1/1 - 1")

    def test_update_normal_args_kwargs(self):
        """test update method with normal args and kwwargs"""
        sq = Square(5)
        sq.update(10)
        self.assertEqual(str(sq), "[Square] (10) 0/0 - 5")
        sq.update(1, 2)
        self.assertEqual(str(sq), "[Square] (1) 0/0 - 2")
        sq.update(1, 2, 3)
        self.assertEqual(str(sq), "[Square] (1) 3/0 - 2")
        sq.update(1, 2, 3, 4)
        self.assertEqual(str(sq), "[Square] (1) 3/4 - 2")
        sq1 = Square(10)
        sq1.update(id=1)
        self.assertEqual(str(sq1), "[Square] (1) 0/0 - 10")
        sq1.update(id=1, size=7)
        self.assertEqual(str(sq1), "[Square] (1) 0/0 - 7")
        sq1.update(id=1, size=7, x=8)
        self.assertEqual(str(sq1), "[Square] (1) 8/0 - 7")
        sq1.update(id=1, size=7, x=8, y=9)
        self.assertEqual(str(sq1), "[Square] (1) 8/9 - 7")

    def test_update_have_both_args_kwargs(self):
        """test update method both args and kwargs passed in"""
        sq = Square(1, 2, 3, 4)
        sq.update(5, id=6)
        self.assertEqual(str(sq), "[Square] (5) 2/3 - 1")
        sq.update(5, id=6, x=7)
        self.assertEqual(str(sq), "[Square] (5) 2/3 - 1")

    def test_update_invalid_attribute(self):
        """test update method with invalid attributes"""
        sq = Square(1, 2, 3, 4)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq.update("aa", "bb", 5, 6)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            sq.update(5, 6, "aa", "bb")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq.update(1, "aa", 5, 6)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            sq.update(1, 3, 5, "aa")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            sq.update(1, 3, 5, -1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            sq.update(5, 6, -2, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sq.update(5, -6, 3, 2)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            sq.update(x=-1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            sq.update(y=-1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sq.update(size=-1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq.update(size="size")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            sq.update(x="x")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            sq.update(y="y")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            sq.update(y="y", x="x")

    def test_dictionary_with_normal_args(self):
        """test to dictionary method with normal args"""
        s1 = Square(10, 2, 3, 4)
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(s1_dictionary, {"id": 4, "size": 10, "x": 2, "y": 3})
        self.assertEqual(dict, type(s1_dictionary))
        s2 = Square(1, 1)
        s2.update(**s1_dictionary)
        s2_dictionary = s2.to_dictionary()
        self.assertEqual(s2_dictionary, s1_dictionary)
        self.assertEqual(dict, type(s2_dictionary))

    def test_dictionary_with_invalid_args(self):
        s1 = Square(10, 2, 1)
        errmsg = 'to_dictionary() takes 1 positional argument but 2 were given'
        with self.assertRaises(TypeError):
            s1_dictionary = s1.to_dictionary({"id": 1, "x": 1, "y": 1})
