# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an n x n binary matrix image, flip the image horizontally then invert
    it, and return the resulting image.

    To flip an image horizontally means that each row of the image is reversed.

    To invert an image mean that each 0 is replaced by 1 and each 1 is replaced
    by 0.
    '''
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        return [[not j for j in i[::-1]] for i in image]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,1,0],[1,0,1],[0,0,0]]
        o = [[1,0,0],[0,1,0],[1,1,1]]
        self.assertEqual(s.flipAndInvertImage(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
        o = [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
        self.assertEqual(s.flipAndInvertImage(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)