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

    def test_to_dictionary(self):
        '''test to_dictionary() method'''
        # Test case 1
        rectangle1 = Rectangle(10, 2, 1, 9)
        expected_output1 = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(rectangle1.to_dictionary(), expected_output1)

        # Test case 2
        rectangle2 = Rectangle(1, 1)
        expected_output2 = {'x': 0, 'y': 0, 'id': 2, 'height': 1, 'width': 1}
        self.assertEqual(rectangle2.to_dictionary(), expected_output2)

        # Test case 3
        rectangle3 = Rectangle(10, 2, 0, 0, 12)
        expected_output3 = {'x': 0, 'y': 0, 'id': 12, 'height': 2, 'width': 10}
        self.assertEqual(rectangle3.to_dictionary(), expected_output3)

    def test_update_args(self):
        '''test update() method with *args'''
        # Test case 1
        rectangle1 = Rectangle(10, 10, 10, 10)
        rectangle1.update(89)
        self.assertEqual(str(rectangle1), "[Rectangle] (89) 10/10 - 10/10")

        # Test case 2
        rectangle2 = Rectangle(10, 10, 10, 10)
        rectangle2.update(89, 2)
        self.assertEqual(str(rectangle2), "[Rectangle] (89) 10/10 - 2/10")

        # Test case 3
        rectangle3 = Rectangle(10, 10, 10, 10)
        rectangle3.update(89, 2, 3)
        self.assertEqual(str(rectangle3), "[Rectangle] (89) 10/10 - 2/3")

        # Test case 4
        rectangle4 = Rectangle(10, 10, 10, 10)
        rectangle4.update(89, 2, 3, 4)
        self.assertEqual(str(rectangle4), "[Rectangle] (89) 4/10 - 2/3")

        # Test case 5
        rectangle5 = Rectangle(10, 10, 10, 10)
        rectangle5.update(89, 2, 3, 4, 5)
        self.assertEqual(str(rectangle5), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        '''test update() method with **kwargs'''
        # Test case 1
        rectangle1 = Rectangle(10, 10, 10, 10)
        rectangle1.update(height=1)
        self.assertEqual(str(rectangle1), "[Rectangle] (1) 10/10 - 10/1")

        # Test case 2
        rectangle2 = Rectangle(10, 10, 10, 10)
        rectangle2.update(width=1, x=2)
        self.assertEqual(str(rectangle2), "[Rectangle] (2) 2/10 - 1/10")

        # Test case 3
        rectangle3 = Rectangle(10, 10, 10, 10)
        rectangle3.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(rectangle3), "[Rectangle] (89) 3/1 - 2/10")

        # Test case 4
        rectangle4 = Rectangle(10, 10, 10, 10)
        rectangle4.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(rectangle4), "[Rectangle] (1) 1/3 - 4/2")

        # Test case 5
        rectangle5 = Rectangle(10, 10, 10, 10)
        rectangle5.update(89, 2, 3, 4, 5, id=98)
        self.assertEqual(str(rectangle5), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_args_kwargs(self):
        '''test update() method with *args and **kwargs'''
        # Test case 1
        rectangle1 = Rectangle(10, 10, 10, 10)
        rectangle1.update(89, 2, 3, 4, x=1, height=2, y=3, width=4)
        self.assertEqual(str(rectangle1), "[Rectangle] (89) 4/10 - 2/3")

        # Test case 2
        rectangle2 = Rectangle(10, 10, 10, 10)
        rectangle2.update(89, x=1, height=2, y=3, width=4)
        self.assertEqual(str(rectangle2), "[Rectangle] (89) 10/10 - 10/10")

        # Test case 3
        rectangle3 = Rectangle(10, 10, 10, 10)
        rectangle3.update(x=1, height=2, y=3, width=4, id=89)
        self.assertEqual(str(rectangle3), "[Rectangle] (89) 10/10 - 4/2")

        # Test case 4
        rectangle4 = Rectangle(10, 10, 10, 10)
        rectangle4.update(89, 2, 3, 4, id=98, x=1, height=2, y=3, width=4)
        self.assertEqual(str(rectangle4), "[Rectangle] (89) 4/10 - 2/3")

    def test_save_to_file(self):
        '''test save_to_file() method'''
        # Test case 1
        rectangle1 = Rectangle(10, 7, 2, 8)
        rectangle2 = Rectangle(2, 4)
        Rectangle.save_to_file([rectangle1, rectangle2])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(
                [rectangle1.to_dictionary(), rectangle2.to_dictionary()],
                Base.from_json_string(f.read())
            )

if __name__ == '__main__':
    unittest.main()
