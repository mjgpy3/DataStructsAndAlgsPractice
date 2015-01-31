#!/usr/bin/env python

import unittest
from assoc_list import AssocList

class AssocListTests(unittest.TestCase):
    def setUp(self):
        self.uut = AssocList()

    def test_insert_can_be_used(self):
        self.uut.insert('answer', 42)

    def test_delete_can_be_used(self):
        self.uut.delete('answer')

    def test_get_can_be_used(self):
        self.uut.get('answer')

    def test_contains_can_be_used(self):
        'answer' in self.uut

if __name__ == '__main__':
    unittest.main()
