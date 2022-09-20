# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given two integer arrays nums1 and nums2, return the maximum length of a
    subarray that appears in both arrays.
    '''
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
        return max(max(r) for r in dp)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,2,1]
        j = [3,2,1,4,7]
        o = 3
        self.assertEqual(s.findLength(i,j), o)

    def test_two(self):
        s = Solution()
        i = [0,0,0,0,0]
        j = [0,0,0,0,0]
        o = 5
        self.assertEqual(s.findLength(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)