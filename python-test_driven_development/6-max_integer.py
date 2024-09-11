#!/usr/bin/python3
"""
unittests
"""
import unittest
from 6-max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
       """
    Parameters:
        unittest.TestCase: tests for lists to find the max int
    """
    def test_positive_integers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_integers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_integers(self):
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)

    def test_single_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        self.assertIsNone(max_integer([])

    def test_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_not_integer_elements(self):
        with self.assertRaises(TypeError):
            max_integer([1, "two", 3])

if __name__ == '__main__':
    unittest.main()


