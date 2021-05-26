#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_simple_max(self):
        self.assertEqual(max_integer([1, 10, 33]), 33)
        self.assertEqual(max_integer([-1, -5, -33]), -1)
        self.assertEqual(max_integer([-1, -0.5, -23]), -0.5)
        self.assertEqual(max_integer([-1]), -1)

    def test_list(self):
        self.assertIsNone(max_integer([]))
        self.assertIsNone(max_integer())

    def test_type(self):
        self.assertIsInstance([], list)


if __name__ == '__main__':
    unittest.main()
