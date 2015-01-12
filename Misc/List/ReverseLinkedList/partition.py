#!/usr/bin/env python

def result_for_2_or_less(items):
    if len(items) == 2 and items[0] >= items[1]:
        return { 'items': items[::-1], 'pivotIndex': 1 }
    return { 'items': items[:], 'pivotIndex': (0 if items else None) }

def partition_around_first(items):
    n = len(items)
    if n <= 2:
        return result_for_2_or_less(items)

    pivot_i, next_i, result = 0, 1, items[:]

    for i in xrange(1, n):
        if result[i] < result[pivot_i]:
            result[i], result[pivot_i] = result[pivot_i], result[i]
            pivot_i = i
        if result[pivot_i] < result[next_i] and pivot_i > next_i:
            result[pivot_i], result[next_i] = result[next_i], result[pivot_i]
            pivot_i = next_i
        next_i = pivot_i+1
    return { 'items': result, 'pivotIndex': pivot_i }

for i in [
        [],
        [1],
        [1, 2],
        [2, 1],
        [2, 2],
        [1, 2, 3],
        [3, 2, 1],
        [7, 2, 2, 1, 9],
        [7, 2, 8, 2, 19, 1, 9],
        ]:
    print i, '->', partition_around_first(i)
