#!/usr/bin/env python

import unittest
from dict_test_cases import DictTestCases
from hash_map import HashMap

class HashMapTests(unittest.TestCase, DictTestCases):
    def setUp(self):
        self.uut = HashMap()

    def mock_hashes_to(self, index = 0):
        class Mock(object):
            def __hash__(self):
                return index

            def __str__(self):
                return "mock(%s)" % index
            __repr__ = __str__
        return Mock()

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

    def test_collisions_are_handled(self):
        first = self.mock_hashes_to(1)
        second = self.mock_hashes_to(1)
        self.uut.insert(first, 'spam')
        self.uut.insert(second, 'eggs')
        self.assertEqual('spam', self.uut.get(first))
        self.assertEqual('eggs', self.uut.get(second))

    def test_inserting_items_with_a_higher_value_works(self):
        item = self.mock_hashes_to(99)
        self.uut.insert(item, 42)

        self.assertEqual(42, self.uut.get(item))

    def test_when_at_doubling_size_then_the_capacity_doubles(self):
        for i in xrange(11):
            self.uut.insert(i, '_')

        self.assertEqual(16, self.uut.capacity())

        self.uut.insert(12, '_')

        self.assertEqual(32, self.uut.capacity())
        self.assertEqual(12, len(self.uut))

    def test_len_is_0_after_delete_of_empty(self):
        self.uut.delete('foo')
        self.assertEqual(0, len(self.uut))

    def test_len_is_0_after_delete_of_only_item(self):
        self.uut.insert('foo', '_')
        self.uut.delete('foo')
        self.assertEqual(0, len(self.uut))

    def test_len_is_0_after_delete_of_only_item_twice(self):
        self.uut.insert('foo', '_')
        self.uut.delete('foo')
        self.uut.delete('foo')
        self.assertEqual(0, len(self.uut))

if __name__ == '__main__':
    unittest.main()
