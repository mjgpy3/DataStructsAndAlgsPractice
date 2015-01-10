#!/usr/bin/env python

def item_at(i, last_layer):
    return (
        (last_layer[i-1] if i > 0 else 0) +
        (last_layer[i] if i < len(last_layer) else 0)
    )

def build(depth, last_layer=None):
    if last_layer is None:
        return [[1]] + build(depth-1, [1])
    if depth == 0:
        return []

    layer = [item_at(i, last_layer) for i in xrange(len(last_layer)+1)]

    return [layer] + build(depth-1, layer)
