#!/usr/bin/env python

import unittest
from assoc_list import AssocList

class AssocListTests(unittest.TestCase):
    def setUp(self):
        self.uut = AssocList()

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

    def test_get_throws_a_key_error_when_sought_item_has_not_been_inserted(self):
        self.assertRaises(KeyError, self.uut.get, ('answer'))

    def test_get_returns_the_sought_keys_value_when_it_has_been_inserted(self):
        self.uut.insert('answer', 42)
        self.assertEqual(42, self.uut.get('answer'))

    def test_when_items_are_re_inserted_the_second_is_gotten(self):
        self.uut.insert('answer', 35)
        self.uut.insert('answer', 42)
        self.assertEqual(42, self.uut.get('answer'))

    def test_when_a_key_is_delete_is_cannot_be_gotten(self):
        self.uut.insert('answer', 42)
        self.uut.delete('answer')
        self.assertRaises(KeyError, self.uut.get, ('answer'))

    def test_when_a_key_that_was_inserted_twice_is_delete_is_cannot_be_gotten(self):
        self.uut.insert('answer', 42)
        self.uut.insert('answer', 35)
        self.uut.delete('answer')
        self.assertRaises(KeyError, self.uut.get, ('answer'))

if __name__ == '__main__':
    unittest.main()
