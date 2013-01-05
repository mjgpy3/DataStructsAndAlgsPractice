#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Fri Jan  4 21:30:39 EST 2013
# 
# 

class Heap(object):
    def __init__(self):
        self.count = 0
        self.root = None

    def heapify(self, iterable):
        for elem in iterable:
            self.add_item(elem)

    def add_item(self, ordinal):
        self.count += 1
        if self.count == 1:
            self.root = Node(ordinal)
            return
        
        i = self.count
        current_node = self.root
        new_node = Node(ordinal)

        while i != 1:
            if current_node.data < new_node.data:
                current_node.data, new_node.data = new_node.data, current_node.data
            if i%2 == 0:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = new_node
            else:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = new_node

            i /= 2

class Node(object):
    def __init__(self, ordinal):
        self.data = ordinal
        self.left = None
        self.right = None

    def __str__(self):
        return "[%s <- %s -> %s]" % (str(self.left) if self.left != None \
                                                    else 'END', str(self.data), \
                                       str(self.right) if self.right != None \
                                                       else 'END')

if __name__ == '__main__':
    heap = Heap()

    a = [12, 61, 323, 42, 36, 35, 1, 90, 982, -9, 123, 1, 61, 92, 12, 0, -23, -3]

    heap.heapify(a)

    print str(heap.root)
    print "Length of a: %d" % len(a)
    print "Length of heap: %d" % heap.count
