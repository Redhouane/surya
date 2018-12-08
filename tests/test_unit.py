# -*- coding: utf-8 -*-

import unittest2
import drealib.paper as paper


class TestDrEA(unittest2.TestCase):  # TODO: Complete the setup for call unit test from Makefile

    def setUp(self):
        """
        Setting up an instance of class Paper
        """

        self.func = paper.Paper()

    def test_1(self):
        """
        Testing creation of class Paper instance
        """

        self.assertTrue(True)

    def test_2(self):
        """
        Testing initial values of Paper instance's attributes
        """

        self.assertEqual(self.func.title, "")
        self.assertEqual(self.func.year, "")
        self.assertEqual(self.func.abstract, "")
        self.assertEqual(self.func.text, "")
        self.assertEqual(self.func.authors, "")
        self.assertEqual(self.func.references, "")


if __name__ == '__main__':
    unittest2.main(verbosity=2)
