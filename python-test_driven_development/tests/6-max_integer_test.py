#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Class for testing max_integer function
    """
    def test_max_integer(self):
        """Positive ints"""
        test_list = [32, 5, 6, 12, 1, 17, 99]
        self.assertEqual(max_integer(test_list), 99)


    def test_max_at_beginning(self):
        """Positive ints with max at beginning"""
        test_list = [99, 1, 6, 2, 88, 33]
        self.assertEqual(max_integer(test_list), 99)


    def test_max_in_middle(self):
        """Positive ints with max in middle"""
        test_list = [5, 99, 1]
        self.assertEqual(max_integer(test_list), 99)


    def test_one_negative_number(self):
        """One negative number"""
        test_list = [1, 5, 99, -12, 55]
        self.assertEqual(max_integer(test_list), 99)


    def test_only_negative_numbers(self):
        """Only negative numbers"""
        test_list = [-99, -12, -55, -2, -9]
        self.assertEqual(max_integer(test_list), -2)


    def test_only_one_element(self):
        """Only one element"""
        test_list = [99]
        self.assertEqual(max_integer(test_list), 99)


    def test_empty_list(self):
        """Empty list"""
        test_list = []
        self.assertEqual(max_integer(test_list), None)
