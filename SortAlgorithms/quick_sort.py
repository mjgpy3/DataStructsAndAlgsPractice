#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Thu Jan  3 19:30:22 EST 2013
# 
# 

from random import choice

def quick_sort(list):
    if len(list) < 2: return list

    greater, less, pivot = [], [], list.pop()

    for elem in list:
        (less if elem < pivot else greater).append(elem)

    return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == '__main__':
    a = [1, 324, 12, 3, 12, 344, 12, 54, 1, 345, 12, 64, 872, 3425, 2]

    print quick_sort(a)
