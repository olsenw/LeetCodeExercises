# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import bisect
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two sorted 0-indexed integer arrays nums1 and nums2 as well as an
    integer k, return the kth (1-based smallest product of num1[i] * mums2[j])
    where 0 <= i < nums1.length and 0 <= j < num2.length.
    '''
    # brute force
    # O(n^2) space
    def kthSmallestProduct_brute(self, nums1: List[int], nums2: List[int], k: int) -> int:
        s = sorted(i * j for i in nums1 for j in nums2)
        return s[k-1]

    def kthSmallestProduct_bail(self, nums1: List[int], nums2: List[int], k: int) -> int:
        p1x, p1y = bisect.bisect_left(nums1, 0), len(nums1) - 1
        n1x, n1y = 0, bisect.bisect(nums1, -1)
        p2x, p2y = bisect.bisect_left(nums2, 0), len(nums2) - 1
        n2x, n2y = 0, bisect.bisect(nums2, -1)
        # # positive, positive
        # pp1, pp2 = bisect.bisect_left(nums1, 0), len(nums2) - 1
        # # positive, negative
        # pn1, pn2 = bisect.bisect_left(nums1, 0), nums2[0]
        # # negative, positive
        # np1, np2 = 0, bisect.bisect_left(nums2, 0)
        # # negative, negative
        # nn1, nn2 = 0, 0
        return
    
    # based on solution by varma_5247
    # https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/solutions/6881305/beginner-freindly-java-c-python-js/?envType=daily-question&envId=2025-06-25
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # count the number of product pairs less than a target
        def helper(target:int):
            answer = 0
            for n in nums1:
                if n == 0:
                    if target >= 0:
                        answer += len(nums2)
                    # note if target is negative unable to count any if n is 0 (0 would always be greater)
                elif n > 0:
                    answer += bisect.bisect(nums2, target // n)
                else:
                    answer += len(nums2) - bisect.bisect_left(nums2, (target // n) + (target % n != 0))
            return answer
        # left, right = -float('inf'), float('inf')
        left, right = -10**10, 10**10
        while left < right:
            mid = left + (right - left) // 2
            count = helper(mid)
            if count < k:
                left = mid + 1
            else:
                right = mid
        return left

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,5]
        j = [3,4]
        k = 2
        o = 8
        self.assertEqual(s.kthSmallestProduct(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = [-4,-2,0,3]
        j = [2,4]
        k = 6
        o = 0
        self.assertEqual(s.kthSmallestProduct(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = [-2,-1,0,1,2]
        j = [-3,-1,2,4,5]
        k = 3
        o = -6
        self.assertEqual(s.kthSmallestProduct(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)