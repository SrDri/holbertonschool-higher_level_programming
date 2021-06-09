#!/usr/bin/python3
""" tests base """
import unittest
import pep8
import os

from models.base import Base
from models.rectangle import Rectangle


class TestBaseClass(unittest.TestCase):
    """ Class test base"""

    def setUp(self):
        """ runs unit test"""
        Base._Base__nb_objects = 0

    def test_docstring(self):
        """ test docstring """
        self.assertIsNotNone(Base.__doc__)

    def test_pep8(self):
        """ pep8 """
        style = pep8.StyleGuide(quiet=True)
        pep = style.check_files(["models/base.py"])
        self.assertEqual(pep.total_errors, 0)

    def test_init_id(self):
        """ init id 0+ """
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)

    def test_init_non_empty_id(self):
        """ init with argument """
        self.assertTrue(Base(1), 1)

    def test_init_2(self):
        """ init 2 instances """
        b1 = Base(69)
        b2 = Base()
        self.assertTrue(b1.id == 69)
        self.assertTrue(b2.id == 1)

    def test_init_of_tree_instances(self):
        """ init 3 instances """
        b1 = Base()
        b2 = Base(69)
        b3 = Base()
        self.assertTrue(b1.id == 1)
        self.assertTrue(b2.id == 69)
        self.assertTrue(b3.id == 2)


if __name__ == '__main__':
    unittest.main()
