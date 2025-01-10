# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    Given n item's value and label as two integer arrays values and labels. Also
    given two integers numWanted and useLimit.

    Task is to find a subset of items with the maximum sum of their values such
    that:
    * The number of items is at most numWanted.
    * The number of items with the same label is at most useLimit.

    Return the maximum sum.
    '''
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        n = len(values)
        order = sorted(range(n), key=lambda x: -values[x])
        c = Counter()
        picks = 0
        answer = 0
        for o in order:
            if picks == numWanted:
                break
            if c[labels[o]] < useLimit:
                picks += 1
                answer += values[o]
            c[labels[o]] += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [5,4,3,2,1]
        j = [1,1,2,2,3]
        k = 3
        l = 1
        o = 9
        self.assertEqual(s.largestValsFromLabels(i,j,k,l), o)

    def test_two(self):
        s = Solution()
        i = [5,4,3,2,1]
        j = [1,3,3,3,2]
        k = 3
        l = 2
        o = 12
        self.assertEqual(s.largestValsFromLabels(i,j,k,l), o)

    def test_three(self):
        s = Solution()
        i = [9,8,8,7,6]
        j = [0,0,0,1,1]
        k = 3
        l = 1
        o = 16
        self.assertEqual(s.largestValsFromLabels(i,j,k,l), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)