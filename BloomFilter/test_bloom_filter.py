#!/usr/bin/env python

from bloom_filter import BloomFilter
import unittest

class BloomFilterTests(unittest.TestCase):
    def test_construction_takes_two_parameters(self):
        BloomFilter(2000, 4)

    def test_can_insert(self):
        bloom = BloomFilter(2000, 4)
        bloom.insert(5)

    def test_can_asked_if_in(self):
        bloom = BloomFilter(2000, 4)
        9 in bloom

    def test_inserted_is_probably_contained(self):
        bloom = BloomFilter(2000, 4)
        bloom.insert(42)
        self.assertTrue(42 in bloom)

    def test_when_nothing_is_inserted_nothing_is_contained(self):
        bloom = BloomFilter(2000, 4)
        self.assertFalse(42 in bloom)
        self.assertFalse(4 in bloom)

if __name__ == '__main__':
    unittest.main()
