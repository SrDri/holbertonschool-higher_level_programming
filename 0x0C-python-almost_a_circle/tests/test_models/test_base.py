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
