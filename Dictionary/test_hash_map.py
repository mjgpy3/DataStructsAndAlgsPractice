#!/usr/bin/env python

import unittest
from dict_test_cases import DictTestCases
from hash_map import HashMap

class HashMapTests(unittest.TestCase):
    def setUp(self):
        self.uut = HashMap()

    def mock_hashes_to(self, index = 0):
        mock = lambda: None
        mock.hash = lambda: 0
        return mock

    def test_initial_current_capacity_is_16(self):
        self.assertEqual(16, self.uut.capacity())

    def test_initial_doubling_size_is_12(self):
        self.assertEqual(12, self.uut.doubling_size())

    def test_when_inialized_with_one_half_then_doubling_size_is_8(self):
        uut = HashMap(0.5)
        self.assertEqual(8, uut.doubling_size())

    def test_initial_len_is_0(self):
        self.assertEqual(0, len(self.uut))

    def test_insertion_increses_size_to_1(self):
        self.uut.insert(self.mock_hashes_to(), 42)

    def test_items_that_were_not_inserted_are_not_in_the_dict(self):
        self.assertFalse(self.mock_hashes_to() in self.uut)

    def test_inserted_items_are_in_the_dict(self):
        self.uut.insert(self.mock_hashes_to(), 42)
        self.assertTrue(self.mock_hashes_to() in self.uut)

    def test_when_a_second_item_is_inserted_the_first_is_still_there(self):
        first = self.mock_hashes_to(1)
        (self
            .uut
            .insert(first, 42)
            .insert(self.mock_hashes_to(2), 99))
        self.assertTrue(first in self.uut)

    def test_when_a_second_item_is_inserted_the_second_is_there(self):
        second = self.mock_hashes_to(1)
        (self
            .uut
            .insert(self.mock_hashes_to(2), 42)
            .insert(second, 99))
        self.assertTrue(second in self.uut)

    def test_get_throws_a_key_error_when_sought_item_has_not_been_inserted(self):
        self.assertRaises(KeyError, self.uut.get, (self.mock_hashes_to(1)))

    def test_get_returns_the_sought_keys_value_when_it_has_been_inserted(self):
        obj = self.mock_hashes_to(1)
        self.uut.insert(obj, 42)
        self.assertEqual(42, self.uut.get(obj))

if __name__ == '__main__':
    unittest.main()
