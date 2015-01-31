#!/usr/bin/env python

import unittest
from assoc_list import AssocList

class AssocListTests(unittest.TestCase):
    def setUp(self):
        self.uut = AssocList()

    def test_insert_can_be_used(self):
        self.uut.insert('answer', 42)

if __name__ == '__main__':
    unittest.main()
