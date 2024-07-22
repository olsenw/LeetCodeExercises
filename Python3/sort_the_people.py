# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of strings names, and an array heights that consists of
    distinct positive integers. Both arrays are of length n.

    For each index i, names[i] and heights[i] denote the name and height of the
    ith person.

    Return names sorted in descending order by the people's heights.
    '''
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [j for i,j in sorted(zip(heights, names), reverse=True)]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["Mary","John","Emma"]
        j = [180,165,170]
        o = ["Mary","Emma","John"]
        self.assertEqual(s.sortPeople(i,j), o)

    def test_two(self):
        s = Solution()
        i = ["Alice","Bob","Bob"]
        j = [155,185,150]
        o = ["Bob","Alice","Bob"]
        self.assertEqual(s.sortPeople(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)