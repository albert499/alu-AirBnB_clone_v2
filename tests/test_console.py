#!/usr/bin/python3
"""
the class TestConsole
"""

import console
import pep8
import unittest
HBNBCommand = console.HBNBCommand


class TestConsole(unittest.TestCase):
    """Class for testing documentation of the console"""
    def test_pep8_console(self):
        """Test that console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['console.py'])
        self.assertEqual(result.total_errors, 2,
                         "Found code style errors (and warnings).")

    def test_pep8_test_console(self):
        """Test that tests/test_console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
