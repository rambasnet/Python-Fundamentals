#! /usr/bin/env python3
"""
unittest for fib functions in fib.py module
"""

import unittest
from fib import fib


class FibTest(unittest.TestCase):
    # optional - executes once and the first
    def setUp(self):
        self.fibSeq = [(1, 1), (2, 1), (3, 2), (10, 55), (20, 6765)]
        print('setUp executed...')

    def test1(self):
        print('test1')
        # assertEqual is defined in TestCase class
        for n, val in self.fibSeq:
            self.assertEqual(fib(n), val)

        self.assertRaises(ValueError, fib, -1)

    def test2(self):
        print('test2')
        # function name can be arbitrary but must start with test or
        # should be runTest
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(10), 55)
        self.assertEqual(fib(20), 6765)

    def test3(self):
        print('test 3')
        self.assertAlmostEqual(22/7, 3.142857, 6)
        #self.assertEqual(22/7, 3.142857)
        pass

    # optional - executes after each test function is executed
    def tearDown(self):
        self.fibElems = None
        print("tearDown executed...")


if __name__ == "__main__":
    unittest.main()
