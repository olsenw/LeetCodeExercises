# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two 0-indexed integer arrays nums1 and nums2 of equal length n and a
    positive integer k. Choose a subsequence of indices from nums1 of length k.
    
    For chosen indices i0, i1, ..., ik-1 the score is defined as:
    * The sum of the selected elements from nums1 multiplied with the minimum of
      the selected elements from nums2.
    * It can be defined simply as: (nums1[i0] + nums1[i1] +...+ nums1[ik - 1]) *
      min(nums2[i0] , nums2[i1], ... ,nums2[ik - 1]).
    
    Return the maximum possible score.

    A subsequence of indices of an array is a set that can be derived from the
    set {0, 1, ..., n-1} by deleting some or no elements.
    '''
    def maxScore_incorrect(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums = sorted(((a,b) for a,b in zip(nums1, nums2)), key=lambda x:(-x[1],-x[0]))
        s = sum(a for a,b in nums[:k])
        return s * nums[k-1][1]

    def maxScore_closer(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums = sorted(((a,b) for a,b in zip(nums1, nums2)), key=lambda x:(-x[1],-x[0]))
        heap = []
        i = 0
        m = 0
        while i < len(nums) and (i < k or nums[i][1] == m):
            m = nums[i][1]
            heapq.heappush(heap, nums[i][0])
            i += 1
        while len(heap) > k:
            heapq.heappop(heap)
        return sum(heap) * m

    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums = sorted(((a,b) for a,b in zip(nums1, nums2)), key=lambda x:(-x[1],-x[0]))
        heap = [a for a,b in nums[:k]]
        heapq.heapify(heap)
        s = sum(heap)
        answer = s * nums[k-1][1]
        for a,b in nums[k:]:
            s += a - heapq.heappushpop(heap, a)
            answer = max(answer, s * b)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,3,3,2]
        j = [2,1,3,4]
        k = 3
        o = 12
        self.assertEqual(s.maxScore(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = [4,2,3,1,1]
        j = [7,5,10,9,6]
        k = 1
        o = 30
        self.assertEqual(s.maxScore(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = [2,1,14,12]
        j = [11,7,13,6]
        k = 3
        o = 168
        self.assertEqual(s.maxScore(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)