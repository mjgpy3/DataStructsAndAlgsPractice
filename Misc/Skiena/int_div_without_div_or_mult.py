#!/usr/bin/env python

import unittest

'''
Skiena, 1-28:
    Write a functoin to perform integer div, without using / or *
'''

def div(n, d):
    if n <= d:
        return int(n==d)

    return 1+div(n-d, d)

class DivTests(unittest.TestCase):
    def test_n_by_n_is_1(self):
        self.assertEqual(1, div(4, 4))

    def test_4_by_2_is_2(self):
        self.assertEqual(2, div(4, 2))

    def test_9_by_10_is_0(self):
        self.assertEqual(0, div(9, 10))

    def test_20_by_5_is_4(self):
        self.assertEqual(4, div(20, 5))


unittest.main()
