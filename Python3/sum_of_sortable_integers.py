# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums of length n.

    An integer k is called sortable if k divides n and it is possible to sort
    nums in non-decreasing order by sequentially performing the following
    operations:
    * Partition nums into consecutive subarrays of length k.
    * Cyclically rotate each subarray independently any number of times to the
      left or the right.
    
    Return an integer denoting the sum of all possible sortable integers k.
    '''
    def sortableIntegers_tle(self, nums: list[int]) -> int:
        def contains(block:list[int], sub:list[int]) -> bool:
            n = len(block)
            m = len(sub)
            for i in range(n-m):
                for j in range(m):
                    if block[i+j] != sub[j]:
                        break
                else:
                    return True
            return False
        n = len(nums)
        s = sorted(nums)
        answer = 0
        for k in range(1,n+1):
            if n % k:
                continue
            b = 0
            for i in range(0, n-k+1, k):
                block = nums[i:i+k] + nums[i:i+k]
                # if s[i:i+k] in block:
                if contains(block, s[i:i+k]):
                    b += 1
                else:
                    break
            if b == n // k:
                answer += k
        return answer

    # based on editorial by Leetcode
    # https://leetcode.com/problems/sum-of-sortable-integers/editorial/?envType=daily-question&envId=2026-10-20
    def sortableIntegers(self, nums: list[int]) -> int:
        # for more information on KMP
        # https://leetcode.com/link/?target=https%3A%2F%2Fleetcode.com%2Fproblems%2Ffind-the-index-of-the-first-occurrence-in-a-string%2F
        def kmp(nums1: list[int], nums2: list[int]) -> bool:
            n,m = len(nums1), len(nums2)
            pi = [0] * m
            j = 0
            for i in range(1,m):
                while j > 0 and nums2[i] != nums2[j]:
                    j = pi[j-1]
                if nums2[i] == nums2[j]:
                    j += 1
                pi[i] = j
            j = 0
            for i in range(n):
                while j > 0 and nums1[i] != nums2[j]:
                    j = pi[j-1]
                if nums1[i] == nums2[j]:
                    j += 1
                if j == m:
                    return True
            return False
        def check(nums1: list[int], nums2: list[int]) -> bool:
            # check if cyclic rotations can work
            return kmp(nums1 + nums1, nums2)
        n = len(nums)
        s = sorted(nums)
        answer = 0
        for k in range(1, n+1):
            if n % k:
                continue
            for i in range(0, n, k):
                if not check(nums[i:i+k], s[i:i+k]):
                    break
            else:
                answer += k
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,1,2]
        o = 3
        self.assertEqual(s.sortableIntegers(i), o)

    def test_two(self):
        s = Solution()
        i = [7,6,5]
        o = 0
        self.assertEqual(s.sortableIntegers(i), o)

    def test_three(self):
        s = Solution()
        i = [5,8]
        o = 3
        self.assertEqual(s.sortableIntegers(i), o)

    def test_four(self):
        s = Solution()
        i = [2,1,4,3]
        o = 2
        self.assertEqual(s.sortableIntegers(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)