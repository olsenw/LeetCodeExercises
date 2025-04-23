# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed integer array nums having length n, an integer
    indexDifference, and an integer valueDifference.

    Find two indices i and j, both in the range [0, n - 1], that satisfy the
    following conditions:
    * abs(i - j) >= indexDifference, and
    * abs(nums[i] - nums[j]) >= valueDifference

    Return an integer array answer, where answer = [i,j] if there are two such
    indices, and answer = [-1, -1] otherwise. If there are multiple choices for
    the two indices, return any of them.

    Note i and j may be equal.
    '''
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+indexDifference, n):
                if abs(nums[i] - nums[j]) >= valueDifference:
                    return [i,j]
        return [-1, -1]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [5,1,4,1]
        j = 2
        k = 4
        o = [0,3]
        self.assertEqual(s.findIndices(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = [2,1]
        j = 0
        k = 0
        o = [0,0]
        self.assertEqual(s.findIndices(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = [1,2,3]
        j = 2
        k = 4
        o = [-1,-1]
        self.assertEqual(s.findIndices(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)