# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two non-increasing 0-indexed integer arrays nums1 and nums2.

    A pair of indices (i,j), where 0 <= i < nums1.length and
    0 <= j < nums2.length, is valid if both i <= j and nums1[i] <= nums2[j]. The
    distance of the pair is j - i.

    Return the maximum distance of any valid pair (i,j). If there are no valid
    pairs, return 0.

    An array arr is non-increasing if arr[i-1] > = arr[i] for every
    1 <= i < arr.length.
    '''
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        m,n = len(nums1), len(nums2)
        i = 0
        answer = 0
        for j in range(n):
            while i < m-1 and nums1[i] > nums2[j]:
                i += 1
            if i <= j and nums1[i] <= nums2[j]:
                answer = max(answer, j - i)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [55,30,5,4,2]
        j = [100,20,10,10,5]
        o = 2
        self.assertEqual(s.maxDistance(i,j), o)

    def test_two(self):
        s = Solution()
        i = [2,2,2]
        j = [10,10,1]
        o = 1
        self.assertEqual(s.maxDistance(i,j), o)

    def test_three(self):
        s = Solution()
        i = [30,29,19,5]
        j = [25,25,25,25,25]
        o = 2
        self.assertEqual(s.maxDistance(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)