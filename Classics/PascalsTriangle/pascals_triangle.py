#!/usr/bin/env python

def build(depth, last_layer=[]):
    if last_layer == []:
        return [[1]] + build(depth-1, [1])
    if depth < 1:
        return []

    layer = []
    for i in xrange(len(last_layer)+1):
        item = 0
        if i-1 >= 0:
            item += last_layer[i-1]
        if i < len(last_layer):
            item += last_layer[i]
        layer.append(item)

    return [layer] + build(depth-1, layer)
