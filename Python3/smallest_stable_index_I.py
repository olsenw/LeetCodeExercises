# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums of length n and an integer k.

    For each index i, define its instability score as
    max(nums[0..i]) - min(nums[i..n-1]).

    In other words:
    * max(nums[0..i]) is the largest value among the elements from index 0 to
      index i.
    * min(nums[i..n-1]) is the smallest value among the elements from index i to
      index n-1.

    An index i is called stable if its instability score is less than or equal
    to k.

    Return the smallest stable index. If no such index exists return -1.
    '''
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        prefix = [nums[0]] * n
        for i in range(1,n):
            prefix[i] = max(nums[i], prefix[i-1])
        suffix = [nums[-1]] * n
        for i in range(n-2,-1,-1):
            suffix[i] = min(nums[i], suffix[i+1])
        answer = prefix[-1]
        index = 0
        stable = False
        for i in range(n-1,-1,-1):
            a = prefix[i] - suffix[i]
            if a <= k:
                stable = True
                answer = min(answer, a)
                index = i
        return index if stable else -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [5,0,1,4]
        j = 3
        o = 3
        self.assertEqual(s.firstStableIndex(i,j), o)

    def test_two(self):
        s = Solution()
        i = [3,2,1]
        j = 1
        o = -1
        self.assertEqual(s.firstStableIndex(i,j), o)

    def test_three(self):
        s = Solution()
        i = [0]
        j = 0
        o = 0
        self.assertEqual(s.firstStableIndex(i,j), o)

    def test_four(self):
        s = Solution()
        i = [0,0]
        j = 0
        o = 0
        self.assertEqual(s.firstStableIndex(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)