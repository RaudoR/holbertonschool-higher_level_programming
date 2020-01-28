#!/usr/bin/python3
"""
This module contains all unittest cases for
Base class
"""
import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle
import sys
from io import StringIO
import json
import os


class TestRectangle(unittest.TestCase):
    """
    Class containing functions to run
    multiple tests
    """
    def setUp(self):
        """
        function to redirect stdout to check
        outpute of functions relying on print
        """
        sys.stdout = StringIO()

    def tearDown(self):
        """
        cleans everything up after running
        setup
        """
        sys.stdout = sys.__stdout__

    def test_pep8_model(self):
        """
        Tests for pep8
        """
        p8 = pep8.StyleGuide(quiet=True)
        p = p8.check_files(['models/rectangle.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_pep8_test(self):
        """
        Tests for pep8
        """
        p8 = pep8.StyleGuide(quiet=True)
        p = p8.check_files(['tests/test_models/test_rectangle.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_0_id(self):
        """
        Tests for id
        """
        Base._Base__nb_objects = 0
        R1 = Rectangle(10, 11)
        R2 = Rectangle(11, 12, 13)
        R3 = Rectangle(12, 13, 14, 15)
        R6 = Rectangle(13, 14, 15, 16, 5)
        R4 = Rectangle(2, 4, 5, 6, 7)
        R5 = Rectangle(3, 45, 4, 2, id="10")
        self.assertEqual(R1.id, 1)
        self.assertEqual(R2.id, 2)
        self.assertEqual(R3.id, 3)
        self.assertEqual(R6.id, 5)
        self.assertEqual(R4.id, 7)
        self.assertEqual(R5.id, "10")

    def test_1_arg(self):
        """
        Test for checking numbers of
        objects
        """
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            Rectangle(10)
            Rectangle()
            Rectangle(x=10, y=20)

    def test_2_TypeError(self):
        """
        Test for check Type Error
        """
        Base._Base__nb_objects = 0
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("Hello", 2)
            Rectangle(True, 1)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, "Hello")
            Rectangle(True, 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3, "Hello")
            Rectangle(True, 2, 4)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 4, 5, "Hello")
            Rectangle(True, 2, 4, 5)

    def test_3_ValueError(self):
        """
        Test for checking value error
        """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-3, 2)
            Rectangle(0, 1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(3, -2)
            Rectangle(1, 0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(3, 2, -2)
            Rectangle(1, 2, 0)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(3, 2, 2, -5)
            Rectangle(1, 2, 3, 0)

    def test_5_area(self):
        """
        Tests for less than 2 args
        """
        with self.assertRaises(TypeError):
            R = Rectangle()
            self.R.area(1)

    def test_6_display(self):
        """
        Test display method. Redirecting stdout to StringIO instance with
        expected output.
        """
        Base._Base__nb_objects = 0
        R1 = Rectangle(2, 4)
        R1O = "##\n" \
              "##\n" \
              "##\n" \
              "##\n"
        R2 = Rectangle(2, 3)
        R2O = "##\n" \
              "##\n" \
              "##\n"
        try:
            R1.display()
            self.assertEqual(sys.stdout.getvalue(), R1O)
        finally:
            sys.stdout.seek(0)
            sys.stdout.truncate(0)
        try:
            R2.display()
            self.assertEqual(sys.stdout.getvalue(), R2O)
        finally:
            sys.stdout.seek(0)
            sys.stdout.truncate(0)

    def test_7_str(self):
        """
        Test that __str__ method produces correct output.
        """
        Base._Base__nb_objects = 0
        R0 = Rectangle(3, 2, 3)
        self.assertEqual(R0.__str__(), "[Rectangle] (1) 3/0 - 3/2")
        R1 = Rectangle(4, 5, 6, 7, 8)
        self.assertEqual(R1.__str__(), "[Rectangle] (8) 6/7 - 4/5")

    def test_8_display_with_xy(self):
        """
        Test display method. Redirecting stdout to StringIO instance with
        expected output.
        """
        Base._Base__nb_objects = 0
        R1 = Rectangle(2, 3, 2, 2)
        R1O = "\n" \
              "\n" \
              "  ##\n" \
              "  ##\n" \
              "  ##\n"
        R2 = Rectangle(3, 2, 1, 0)
        R2O = " ###\n" \
              " ###\n"
        try:
            R1.display()
            self.assertEqual(sys.stdout.getvalue(), R1O)
        finally:
            sys.stdout.seek(0)
            sys.stdout.truncate(0)
        try:
            R2.display()
            self.assertEqual(sys.stdout.getvalue(), R2O)
        finally:
            sys.stdout.seek(0)
            sys.stdout.truncate(0)
