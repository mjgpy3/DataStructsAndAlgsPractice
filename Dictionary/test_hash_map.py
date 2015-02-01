#!/usr/bin/env python

import unittest
# from dict_test_cases import DictTestCases
from hash_map import HashMap

class AssocListTests(unittest.TestCase):#, DictTestCases):
    def setUp(self):
        self.uut = HashMap()

    def test_initial_current_capacity_is_16(self):
        self.assertEqual(16, self.uut.capacity())

    def test_initial_doubling_size_is_12(self):
        self.assertEqual(12, self.uut.doubling_size())

    def test_when_inialized_with_one_half_then_doubling_size_is_8(self):
        uut = HashMap(0.5)
        self.assertEqual(8, uut.doubling_size())

if __name__ == '__main__':
    unittest.main()
