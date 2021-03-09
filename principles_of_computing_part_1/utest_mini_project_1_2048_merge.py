#!/usr/bin/env python2

import unittest
import mini_project_1_2048_merge as project_2048

class TestMerge(unittest.TestCase):
    def test_result(self):
        self.assertEqual(project_2048.merge([2, 0, 2, 4]), [4, 4, 0, 0])
        self.assertEqual(project_2048.merge([0, 0, 2, 2]), [4, 0, 0, 0])
        self.assertEqual(project_2048.merge([2, 2, 0, 0]), [4, 0, 0, 0])
        self.assertEqual(project_2048.merge([2, 2, 2, 2, 2]), [4, 4, 2, 0, 0])
        self.assertEqual(project_2048.merge([8, 16, 16, 8]), [8, 32, 8, 0])
        self.assertEqual(project_2048.merge([0]), [0])
        self.assertEqual(project_2048.merge([3, 5, 1, 3, 3, 6]), [3, 5, 1, 6, 6, 0])
        self.assertEqual(project_2048.merge([2]), [2])
        self.assertEqual(project_2048.merge([2, 0, 4]), [2, 4, 0])
        self.assertEqual(project_2048.merge([2, 2]), [4, 0])
        self.assertEqual(project_2048.merge([4, 2]), [4, 2])
        self.assertEqual(project_2048.merge([0, 2]), [2, 0])
        self.assertEqual(project_2048.merge([0, 0, 0]), [0, 0, 0])
        self.assertEqual(project_2048.merge([0, 0, 0, 0, 4]), [4, 0, 0, 0, 0])

if __name__ == '__main__':
    unittest.main()
