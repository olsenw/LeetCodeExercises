# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of distinct integers arr and an array of integer arrays
    pieces, where the integers in pieces are distinct. The goal is to form arr
    by concatenating the arrays in pieces in any order. However, it is not
    allowed to reorder teh integers in each array pieces[i].

    Return true if it is possible to form the array arr from pieces. Otherwise,
    return false.

    Note the integers in arr are distinct and the integers in pieces are
    distinct.
    '''
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        try:
            for p in pieces:
                i = arr.index(p[0])
                for j in range(len(p)):
                    if arr[i+j] != p[j]:
                        return False
        except:
            return False
        return True

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [15,88]
        j = [[88],[15]]
        o = True
        self.assertEqual(s.canFormArray(i,j), o)

    def test_two(self):
        s = Solution()
        i = [49,18,16]
        j = [[16,18,49]]
        o = False
        self.assertEqual(s.canFormArray(i,j), o)

    def test_three(self):
        s = Solution()
        i = [91,4,64,78]
        j = [[78],[4,64],[91]]
        o = True
        self.assertEqual(s.canFormArray(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)