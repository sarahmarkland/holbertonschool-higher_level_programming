'''test_rectangle module'''
import unittest
import sys
from io import StringIO
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    '''class docstring for TestRectangle'''
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

    def setUp(self):
        '''custom method to redirect stdout to a StingIO object to
        capture printed output'''
        self.output = StringIO()
        sys.stdout = self.output

    def tearDown(self):
        '''restore standard output'''
        sys.stdout = sys.__stdout__

    def test_display1(self):
        '''create Rectangle instances with varying width/height and 
        compare output to expected result'''
        # Test case 1: Width = 4, Height = 5
        rectangle1 = Rectangle(4, 5)
        rectangle1.display()
        self.assertEqual(self.output.getvalue(), "####\n####\n####\n####\n####\n")

    def test_display2(self):
        '''create Rectangle instances with varying width/height and 
        compare output to expected result'''
        # Test case 2: Width = 7, Height = 3
        rectangle2 = Rectangle(7, 3)
        rectangle2.display()
        self.assertEqual(self.output.getvalue(), "#######\n#######\n#######\n")

    def test_display3(self):
        '''create Rectangle instances with varying width/height and 
        compare output to expected result'''
        # Test case 3: Width = 2, Height = 2
        rectangle3 = Rectangle(2, 2)
        rectangle3.display()
        self.assertEqual(self.output.getvalue(), "##\n##\n")

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
