#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Thu Jan 17 16:14:36 EST 2013
# 
# 

from random import randrange

a = [randrange(0, 15) for i in xrange(10)]

def set_print(list, index, name):
    print name, "set to", index, ", list[" + name + "] =", list[index]

def swap(list, i_1, i_2):
    list[i_1], list[i_2] = list[i_2], list[i_1]

def partition(list):
    print list
    i_p = len(list)-1
    i_r = i_p-1
    i_l = 0
    set_print(list, i_p, 'i_p')
    set_print(list, i_r, 'i_r')
    set_print(list, i_l, 'i_l')

    while i_l < i_p:
        if list[i_r] > list[i_p] and list[i_l] < list[i_p]:
            swap(list, i_p, i_r)
            i_p -= 1

        elif list[i_l] > list[i_p] and list[i_r] > list[i_p]:
            swap(list, i_r, i_p)
            i_p -= 1
            swap(list, i_l, i_p)
            

        elif list[i_r] > list[i_p]:
            swap(list, i_r, i_p)
            i_p -= 1

        i_r = i_p-1 
        i_l += 1
        print a
    
partition(a)
