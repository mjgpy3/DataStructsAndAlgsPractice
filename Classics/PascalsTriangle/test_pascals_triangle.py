#!/usr/bin/env python

import unittest
import pascals_triangle

class BuildPascalsTriangleTest(unittest.TestCase):
    def test_build_with_depth_of_1_is_just_1(self):
        self.assertEqual([[1]], pascals_triangle.build(1))

    def test_build_with_depth_of_2_is_1_and_1_1(self):
        self.assertEqual([[1], [1, 1]], pascals_triangle.build(2))

    def test_build_with_depth_of_2_is_1_and_1_1_and_1_2_1(self):
        self.assertEqual([[1], [1, 1], [1, 2, 1]], pascals_triangle.build(3))

    def test_works_for_5(self):
        self.assertEqual([
            [1], 
            [1, 1], 
            [1, 2, 1], 
            [1, 3, 3, 1], 
            [1, 4, 6, 4, 1]], pascals_triangle.build(5))

unittest.main()
