#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Wed Jan  2 13:28:20 EST 2013
# 
# 

def binary_search(the_list, val, beg=0, end=None):
    """
        Searches through a sorted list for a specific value.
        If not found, returns None
    """
    if end == None:
        end = len(the_list)

    half = (beg + end)/2

    if the_list[half] == val:
        return half
    elif half == beg or half == end:
        return None
    elif the_list[half] < val:
        return binary_search(the_list, val, half, end)
    else:
        return binary_search(the_list, val, beg, half)

def verbose_searcher(search_me, value, function):
    search_me.sort()
    print search_me
    print value, "found at", function(search_me, value)


if __name__ == '__main__':
    search_me = [14,234,1,63,123,54,1,6,1,4,7,2,71,234]

    verbose_searcher(search_me, 4)
    verbose_searcher(search_me, 911) 

    search_me = ['Michael', 'casio', 'hobbit', 'Django', 'Zebra', 'notebook']

    verbose_searcher(search_me, 'Michael')
    verbose_searcher(search_me, "FooBar")

    for thing in search_me:
        verbose_searcher(search_me, thing)
