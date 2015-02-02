#!/usr/bin/env python

from bloom_filter import BloomFilter
import unittest

class BloomFilterTests(unittest.TestCase):
    def test_construction_takes_two_parameters(self):
        BloomFilter(2000, 4)

    def test_can_insert(self):
        bloom = BloomFilter(2000, 4)
        bloom.insert(5)


if __name__ == '__main__':
    unittest.main()
