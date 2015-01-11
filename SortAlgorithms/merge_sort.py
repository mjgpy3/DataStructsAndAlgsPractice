#!/usr/bin/env python

import unittest

def merge(left, right):
    result = []
    while left or right:
        if left and right:
            result.append((left if left[0] <= right[0] else right).pop(0))
        else:
            result.append((left or right).pop(0))
    return result


def merge_sort(items):
    if len(items) < 2: return items

    middle = len(items)/2

    return merge(
        merge_sort(items[:middle]),
        merge_sort(items[middle:])
    )

class MergeSortTests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual([], merge_sort([]))

    def test_single_element(self):
        self.assertEqual([1], merge_sort([1]))

    def test_multiple_elements(self):
        self.assertEqual([-10, 0, 0, 9, 9, 19, 72], merge_sort([0, 9, -10, 0, 9, 19, 72]))

if __name__ == '__main__':
    unittest.main()
