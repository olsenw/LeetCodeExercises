# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

from sortedcontainers import SortedList

class Solution:
    '''
    Given an array of integers nums and an integer limit, return the size of the
    longest non-empty subarray such that the absolute difference between any two
    elements of this subarray is less than or equal to limit.
    '''
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        answer = 0
        s = SortedList()
        i = 0
        for j in range(len(nums)):
            s.add(nums[j])
            while abs(s[-1] - s[0]) > limit:
                s.remove(nums[i])
                i += 1
            answer = max(answer, len(s))
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [8,2,4,7]
        j = 4
        o = 2
        self.assertEqual(s.longestSubarray(i,j), o)

    def test_two(self):
        s = Solution()
        i = [10,1,2,4,7,2]
        j = 5
        o = 4
        self.assertEqual(s.longestSubarray(i,j), o)

    def test_three(self):
        s = Solution()
        i = [4,2,2,2,4,4,2,2]
        j = 0
        o = 3
        self.assertEqual(s.longestSubarray(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)