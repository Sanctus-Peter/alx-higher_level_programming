#!/usr/bin/python3
"""Module for Base class tests"""
import unittest
from models.base import Base


class TestBaseMethods(unittest.TestCase):
    """To test Base class"""

    def setUp(self) -> None:
        Base._Base__nb_objects = 0

    def test_id(self):
        val1 = Base(21)
        val2 = Base()
        val3 = Base()
        val4 = Base()
        self.assertEqual(val1.id, 21)
        self.assertEqual(val3.id, val4.id - 1)
        self.assertEqual(val2.id, 1)
