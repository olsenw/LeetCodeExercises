# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed integer array nums of length n and an integer k, return
    the number of pairs (i,j) where 0 <= 1 < j < n, such that nums[i] == nums[j]
    and (i * j) is divisible by k.
    '''
    # brute force
    def countPairs(self, nums: List[int], k: int) -> int:
        return sum(nums[i] == nums[j] and i * j % k == 0 for i in range(len(nums)) for j in range(i+1, len(nums)))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,1,2,2,2,1,3]
        j = 2
        o = 4
        self.assertEqual(s.countPairs(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,4]
        j = 1
        o = 0
        self.assertEqual(s.countPairs(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)