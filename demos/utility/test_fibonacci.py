#! /usr/bin/env python3

"""
unittest for fib functions in fib.py module
"""

import unittest
from utility.fibonacci import fib


class FibTest(unittest.TestCase):
    # optional - executes before each test function
    def setUp(self):
        self.fib_seq = [(1, 1), (2, 1), (3, 2), (10, 55), (20, 6765)]
        print('setUp executed...')

    # any function that start with test* will be executed automatically
    def test1(self):
        # assertEqual is defined in TestCase class
        for n, val in self.fib_seq:
            self.assertEqual(fib(n), val)

    def test2(self):
        # function name can be arbitrary but must start with test or
        # should be runTest
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(10), 55)
        self.assertEqual(fib(20), 6765)

    def test3(self):
        # doesn't test fib function but gets called...
        self.assertAlmostEqual(22/7, 3.142857, 6)
        # uncomment the following and run it
        # self.assertEqual(22/7, 3.142857)
        pass

    def testException(self):
        print('test exception')
        # notice function is not called but is is passed along with the parameter
        self.assertRaises(ValueError, fib, -1)

    # function without test word in name
    def someTest(self):
        print('someTest')
        print('This function will not run!')

    # optional - executes after each test function is executed
    def tearDown(self):
        self.fibElems = None
        print("tearDown executed...")
