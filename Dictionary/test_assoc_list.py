#!/usr/bin/env python

import unittest
from dict_test_cases import DictTestCases
from assoc_list import AssocList

class AssocListTests(unittest.TestCase, DictTestCases):
    def setUp(self):
        self.uut = AssocList()

if __name__ == '__main__':
    unittest.main()
