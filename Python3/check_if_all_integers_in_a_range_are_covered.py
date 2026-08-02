# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 2D integer array ranges and two integers left and right. Each
    ranges[i] = [starti, endi] represents an inclusive interval between starti
    and endi.

    Return true if each integer in the inclusive range [left, right] is covered
    by at least one interval in ranges. Return false otherwise.

    An integer x is covered by an interval ranges[i] = [starti, endi] if 
    starti <= x <= endi.
    '''
    # brute force it (range is very small)
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        covered = [False] * 51
        for i,j in ranges:
            for k in range(i,j+1):
                covered[k] = True
        return all(covered[k] for k in range(left, right+1))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,2],[3,4],[5,6]]
        j = 2
        k = 5
        o = True
        self.assertEqual(s.isCovered(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = [[1,10],[10,20]]
        j = 21
        k = 21
        o = False
        self.assertEqual(s.isCovered(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)