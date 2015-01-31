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
        (self
            .uut
            .insert('answer', 42)
            .insert('spaz', 99))
        self.assertTrue('answer' in self.uut)

    def test_when_a_second_item_is_inserted_the_second_is_there(self):
        (self
            .uut
            .insert('answer', 42)
            .insert('spaz', 99))
        self.assertTrue('spaz' in self.uut)

    def test_get_throws_a_key_error_when_sought_item_has_not_been_inserted(self):
        self.assertRaises(KeyError, self.uut.get, ('answer'))

    def test_get_returns_the_sought_keys_value_when_it_has_been_inserted(self):
        self.uut.insert('answer', 42)
        self.assertEqual(42, self.uut.get('answer'))

    def test_when_items_are_re_inserted_the_second_is_gotten(self):
        (self
            .uut
            .insert('answer', 35)
            .insert('answer', 42))
        self.assertEqual(42, self.uut.get('answer'))

    def test_when_a_key_is_delete_is_cannot_be_gotten(self):
        (self
            .uut
            .insert('answer', 42)
            .delete('answer'))
        self.assertRaises(KeyError, self.uut.get, ('answer'))

    def test_when_a_key_that_was_inserted_twice_is_delete_is_cannot_be_gotten(self):
        (self
            .uut
            .insert('answer', 42)
            .insert('answer', 35)
            .delete('answer'))
        self.assertRaises(KeyError, self.uut.get, ('answer'))

    def test_insert_delete_then_insert_can_be_gotten(self):
        (self.uut.insert('answer', 42)
            .delete('answer')
            .insert('answer', 35))
        self.assertEqual(35, self.uut.get('answer'))

    def test_delete_works_when_no_items_are_inserted(self):
        self.uut.delete('no existy')

    def test_e2e_1(self):
        (self
            .uut
            .insert('a', 99)
            .insert('b', 100)
            .insert('c', 72)
            .insert('a', 100)
        )
        for k, v in [['a', 100], ['b', 100], ['c', 72]]:
            self.assertEqual(v, self.uut.get(k))
            self.assertTrue(k in self.uut)
            self.assertFalse(v in self.uut)

        (self
            .uut
            .delete('a')
            .delete('b')
            .delete('c')
            .delete('d')
            .delete('e')
        )
        for k in ['a', 'b', 'c', 'd']:
            self.assertRaises(KeyError, self.uut.get, (k))
            self.assertFalse(k in self.uut)

if __name__ == '__main__':
    unittest.main()
