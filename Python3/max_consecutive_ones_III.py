# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a binary array nums and an integer k, return the maximum number of
    consecutive 1's in the array if it is possible to flip at most k 0's.
    '''
    def longestOnes(self, nums: list[int], k: int) -> int:
        answer = 0
        used = 0
        i = 0
        for j in range(len(nums)):
            while used > k:
                if nums[i] == 0:
                    used -= 1
                i += 1
            if nums[j] == 0:
                used += 1
            if used <= k:
                answer = max(answer, j - i + 1)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,1,1,0,0,0,1,1,1,1,0]
        j = 2
        o = 6
        self.assertEqual(s.longestOnes(i,j), o)

    def test_two(self):
        s = Solution()
        i = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
        j = 3
        o = 10
        self.assertEqual(s.longestOnes(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)