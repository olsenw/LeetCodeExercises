# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums of length n.

    A partition is defined as an index i where 0 <= i < n - 1, splitting the
    array into two non-empty subarrays such that:
    * Left subarray contains indices [0, i].
    * Right subarray contains indices [i+1, n-1].

    Return the number of partitions where the difference between the sum of the
    left and right and right subarrays is even.
    '''
    def countPartitions(self, nums: List[int]) -> int:
        s = sum(nums)
        r = 0
        answer = 0
        for n in nums[:-1]:
            r += n
            s -= n
            answer += (s - r) % 2 == 0
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [10,10,3,7,6]
        o = 4
        self.assertEqual(s.countPartitions(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,2]
        o = 0
        self.assertEqual(s.countPartitions(i), o)

    def test_three(self):
        s = Solution()
        i = [2,4,6,8]
        o = 3
        self.assertEqual(s.countPartitions(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)