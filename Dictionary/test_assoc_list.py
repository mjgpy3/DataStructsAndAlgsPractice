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

    def test_items_that_were_not_inserted_are_not_in_the_dict(self):
        self.assertFalse('answer' in self.uut)

    def test_inserted_items_are_in_the_dict(self):
        self.uut.insert('answer', 42)
        self.assertTrue('answer' in self.uut)

    def test_when_a_second_item_is_inserted_the_first_is_still_there(self):
        self.uut.insert('answer', 42)
        self.uut.insert('spaz', 99)
        self.assertTrue('answer' in self.uut)

    def test_when_a_second_item_is_inserted_the_second_is_there(self):
        self.uut.insert('answer', 42)
        self.uut.insert('spaz', 99)
        self.assertTrue('spaz' in self.uut)

if __name__ == '__main__':
    unittest.main()
