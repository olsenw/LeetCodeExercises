# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed integer array nums, where nums[i] represents the score of
    the ith student. Also given is an integer k.

    Pick the scores of any k students from the array so that the difference
    between the highest and the lowest of the k scores is minimized.

    Return the minimum possible difference.
    '''
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        answer = float('inf')
        for i in range(len(nums) - k + 1):
            answer = min(answer, nums[i+k-1] - nums[i])
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [90]
        j = 1
        o = 0
        self.assertEqual(s.minimumDifference(i,j), o)

    def test_two(self):
        s = Solution()
        i = [9,4,1,7]
        j = 2
        o = 2
        self.assertEqual(s.minimumDifference(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)