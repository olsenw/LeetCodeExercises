# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    Given two integer arrays of equal length target and arr. In one step, is is
    possible to select any non-empty subarray of arr and reverse it. Any number
    of steps are allowed.

    Return true if it is possible to make arr equal to target or false
    otherwise.
    '''
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        c = Counter(arr)
        for t in target:
            c[t] -= 1
        return all(v == 0 for v in c.values())

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,4]
        j = [2,4,1,3]
        o = True
        self.assertEqual(s.canBeEqual(i,j), o)

    def test_two(self):
        s = Solution()
        i = [7]
        j = [7]
        o = True
        self.assertEqual(s.canBeEqual(i,j), o)

    def test_three(self):
        s = Solution()
        i = [3,7,9]
        j = [3,7,11]
        o = False
        self.assertEqual(s.canBeEqual(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)