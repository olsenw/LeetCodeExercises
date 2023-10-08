# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two arrays nums1 and nums2.

    Return thr maximum dot product between two non-empty subsequences of nums1
    and nums2 with the same length.

    A subsequence of a array is a new array which is formed from the original
    array by deleting some (can be none) of the character without disturbing the
    relative positions of the remaining characters.

    dot([a,b,c],[x,y,z]) = a * x + b * y + c * z
    Note that vectors must be of equal length.
    '''
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        # i is the index in nums1 and j is the index in nums2
        @cache
        def dp(i,j):
            if i == len(nums1) or j == len(nums2):
                return 0
            # answer = 0
            # for x in range(i, len(nums1)):
            #     # answer = max(answer, answer + dp(x + 1, j))
            #     for y in range(j, len(nums2)):
            #         answer = max(
            #             answer,
            #             dp(x + 1, y),
            #             dp(x, y + 1),
            #             nums1[x] * nums2[y] + dp(x + 1, y + 1)
            #             )
            # return answer
            # This does not have all the repeated calculation of above
            return max(
                dp(i + 1, j),
                dp(i, j + 1),
                nums1[i] * nums2[j] + dp(i + 1, j + 1)
            )
        return max(nums1[i] * nums2[j] + dp(i + 1, j + 1) for i in range(len(nums1)) for j in range(len(nums2)))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,1,-2,5]
        j = [3,0,-6]
        o = 18
        self.assertEqual(s.maxDotProduct(i,j), o)

    def test_two(self):
        s = Solution()
        i = [3,-2]
        j = [2,-6,7]
        o = 21
        self.assertEqual(s.maxDotProduct(i,j), o)

    def test_three(self):
        s = Solution()
        i = [-1,-1]
        j = [1,1]
        o = -1
        self.assertEqual(s.maxDotProduct(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)