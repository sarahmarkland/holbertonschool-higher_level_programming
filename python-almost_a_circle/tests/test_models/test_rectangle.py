'''test_rectangle module'''
import unittest
import os
import sys
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    '''class docstring for TestRectangle'''
    def setUp(self):
        '''redirect stdout to check output from display()'''
        self.output = StringIO()
        sys.stdout = self.output

        self.rectangle = Rectangle(4, 5)

        # reset nb_objects to 0 before each test
        Base._Base__nb_objects = 0

    def tearDown(self):
        '''clean up after test_display() to restore stdout'''
        sys.stdout = sys.__stdout__

        del self.rectangle
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass
    def test_valid_attributes(self):
        '''test valid attribute values'''
        rectangle = Rectangle(10, 20, 5, 5)
        self.assertEqual(rectangle.width, 10)
        self.assertEqual(rectangle.height, 20)
        self.assertEqual(rectangle.x, 5)
        self.assertEqual(rectangle.y, 5)

    def test_invalid_width(self):
        '''test invalid width values (non-int & value <= 0)'''
        with self.assertRaises(TypeError):
            Rectangle("invalid", 20, 5, 5)

        with self.assertRaises(ValueError):
            Rectangle(0, 20, 5, 5)

        with self.assertRaises(ValueError):
            Rectangle(-10, 20, 5, 5)

    def test_invalid_height(self):
        '''test invalid height values (non-int & value <= 0)'''
        with self.assertRaises(TypeError):
            Rectangle(10, "invalid", 5, 5)

        with self.assertRaises(ValueError):
            Rectangle(0, 20, 5, 5)

        with self.assertRaises(ValueError):
            Rectangle(10, -5, 5, 5)

        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_invalid_x(self):
        '''test invalid x values (non-int & value <= 0)'''

        with self.assertRaises(TypeError):
            Rectangle(10, 20, "invalid", 5)

        with self.assertRaises(ValueError):
            Rectangle(10, 20, -5, 5)

    def test_invalid_y(self):
        '''test invalid y values (non-int & value <= 0)'''

        with self.assertRaises(TypeError):
            Rectangle(10, 20, 5, "invalid")

        with self.assertRaises(ValueError):
            Rectangle(10, 20, 5, -5)

    def test_area(self):
        '''test if Rectangle instances calculate area properly '''
        # Test case 1: Width = 4, Height = 5
        rectangle1 = Rectangle(4, 5)
        self.assertEqual(rectangle1.area(), 20)

        # Test case 2: Width = 7, Height = 3
        rectangle1 = Rectangle(7, 3)
        self.assertEqual(rectangle1.area(), 21)

        # Test case 3: Width = 10, Height = 10
        rectangle1 = Rectangle(10, 10)
        self.assertEqual(rectangle1.area(), 100)

    def test_display(self):
        '''test display() method'''
        self.rectangle = Rectangle(4, 5)
        self.rectangle.display()
        self.assertEqual(self.output.getvalue(),
                                    "####\n####\n####\n####\n####\n")

    def test_display_with_x(self):
        # Test display with x
        self.rectangle = Rectangle(2, 2, 2)
        self.rectangle.display()
        self.assertEqual(self.output.getvalue(), "  ##\n  ##\n")

    def test_display_with_y(self):
        # Test display with x and y
        self.rectangle = Rectangle(2, 2, 2, 2)
        self.rectangle.display()
        self.assertEqual(self.output.getvalue(), "\n\n  ##\n  ##\n")    

    def test_str1(self):
        '''compare the output of str(rectangle) with the expected output'''
        # Test case 1
        rectangle1 = Rectangle(4, 5, 2, 3, 1)
        expected_output1 = "[Rectangle] (1) 2/3 - 4/5"
        self.assertEqual(str(rectangle1), expected_output1)

    def test_str2(self):
        '''compare the output of str(rectangle) with the expected output'''
        # Test case 2
        rectangle2 = Rectangle(7, 3, 1, 2, 2)
        expected_output2 = "[Rectangle] (2) 1/2 - 7/3"
        self.assertEqual(str(rectangle2), expected_output2)

    def test_str3(self):
        '''compare the output of str(rectangle) with the expected output'''
        # Test case 3
        rectangle3 = Rectangle(2, 2, 0, 0, 3)
        expected_output3 = "[Rectangle] (3) 0/0 - 2/2"
        self.assertEqual(str(rectangle3), expected_output3)

if __name__ == '__main__':
    unittest.main()
