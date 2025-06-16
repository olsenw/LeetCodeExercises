# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed integer array nums of size n, find the maximum difference
    between nums[i] and nums[j] (i.e., nums[j] - nums[i]), such that 
    0 <= i < j < n and nums[i] < nums[j].

    Return the maximum difference. If no such i and j exists, return -1.
    '''
    def maximumDifference(self, nums: List[int]) -> int:
        answer = -1
        m = nums[0]
        for n in nums[1:]:
            if n > m:
                answer = max(answer, n - m)
            if n < m:
                m = n
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [7,1,5,4]
        o = 4
        self.assertEqual(s.maximumDifference(i), o)

    def test_two(self):
        s = Solution()
        i = [9,4,3,2]
        o = -1
        self.assertEqual(s.maximumDifference(i), o)

    def test_three(self):
        s = Solution()
        i = [1,5,2,10]
        o = 9
        self.assertEqual(s.maximumDifference(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)