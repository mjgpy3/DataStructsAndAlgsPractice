#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Thu Jan  3 18:02:47 EST 2013
# 
# 

def insertion_sort(list):
    for i in xrange(1, len(list)):
        k = i
        item = list[i]
        while k > 0 and item < list[k-1]:
            list[k] = list[k-1]
            k -= 1
        list[k] = item

if __name__ == '__main__':
    sort_me = [1, 43, 123, 5, 2, 654, 23, 4, 123]
    insertion_sort(sort_me)
    print sort_me

    sort_me = [134, 21, "Michael", 24, 1, "Foobar", 'foobar', "Django Unchained", 23, 12, 1, "j"]
    insertion_sort(sort_me)
    print sort_me
