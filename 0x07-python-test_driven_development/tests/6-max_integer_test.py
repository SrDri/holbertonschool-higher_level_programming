#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 6]), 6)

    def max_beging(self):
        self.assertEqual(max_integer([10, 2, 3, 4, 5, 6]), 10)

    def max_middle(self):
        self.assertEqual(max_integer([1, 2, 20, 4, 5]), 20)
        self.assertEqual(max_integer([-1, -0.5, -23]), -0.5)

    def test_basic_negative(self):
        self.assertEqual(max_integer([-5, -1]), -1)

    def one_element(self):
        self.assertEqual(max_integer([1]), 1)

    def test_list_empty(self):
        self.assertEqual(max_integer([]), None)


if __name__ == '__main__':
    unittest.main()
