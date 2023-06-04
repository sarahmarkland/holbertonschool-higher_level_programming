import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
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
            Rectangle(10, -20, 5, 5)

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

if __name__ == '__main__':
    unittest.main()