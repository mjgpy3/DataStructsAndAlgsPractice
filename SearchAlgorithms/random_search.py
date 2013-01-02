#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Wed Jan  2 17:15:40 EST 2013
# 
# 

from random import choice

def random_search(search_me, val):
    """
        Searches `search_me` for `val` by selecting random values
    """
    indicies = range(len(search_me))

    while indicies != []:
        i = choice(indicies)
        indicies.remove(i)

        if search_me[i] == val:
            return i

    return None

def veribose_search(the_list, val):
    print the_list
    print val, "was found at", random_search(the_list, val)

if __name__ == '__main__':
    a = ["Michael", 2, 4, 7, "Django", "Money", set([1,3,4])]
    veribose_search(a, 35)

    for i in a:
        veribose_search(a, i)
