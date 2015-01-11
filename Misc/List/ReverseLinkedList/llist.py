#!/usr/bin/env python

import unittest

ListEnding = lambda: None

class Node(object):
    @classmethod
    def from_list(cls, list):
        return Node(list[0], Node.from_list(list[1:])) if list else ListEnding

    def reverse(self, last=None):
        if not last:
            return self.next.reverse(Node(self.value, ListEnding))
        
        if self.next == ListEnding:
            return Node(self.value, last)
        else:
            return self.next.reverse(Node(self.value, last))


    def __init__(self, value, next):
        self.value = value
        self.next = next

    def __iter__(self):
        yield self.value
        next = self.next
        while next != ListEnding:
            yield next.value
            next = next.next

class LinkedListTests(unittest.TestCase):
    def test_conversion_to_list_works(self):
        self.assertEqual([1, 2, 3, 4], list(Node(1, Node(2, Node(3, Node(4, ListEnding))))))

    def test_conversion_from_list_works(self):
        self.assertEqual([1, 2, 3, 4], list(Node.from_list([1, 2, 3, 4])))

    def test_reversing_works(self):
        self.assertEqual([4, 3, 2, 1], list(Node.from_list([1, 2, 3, 4]).reverse()))

unittest.main()
