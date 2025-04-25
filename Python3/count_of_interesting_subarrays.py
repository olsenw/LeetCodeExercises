# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed integer array nums, an integer modulo, and an integer k.

    Find the count of subarrays that are interesting.

    A subarray nums[l..r] is interesting if the following condition holds:
    * Let cnt be the number of indices i in the range [l, r] such that
      nums[i] % modulo == k. Then, cnt % modulo == k.
    
    Return an integer denoting the count of interesting subarrays.

    Note: A subarray is a contiguous non-empty sequence of elements within an
    array.
    '''
    # time limit exceeded 609/617
    # O(n^2)
    def countInterestingSubarrays_tle(self, nums: List[int], modulo: int, k: int) -> int:
        answer = 0
        valid = [-1] + [i for i in range(len(nums)) if nums[i] % modulo == k] + [len(nums)]
        # find number of subsequences that dont have valid modulo
        if k == 0:
            k += modulo
            for r in range(1, len(valid)):
                l = r - 1
                s = valid[l]
                e = valid[r]
                n = max(0, e - s - 1)
                answer += (n * (n + 1)) // 2
        valid[0] = -1
        # how many elements to pick from valid
        for w in range(k, len(valid), modulo):
            for r in range(w, len(valid)-1):
                l = r - w + 1
                s = max(1, valid[l] - valid[l-1])
                e = max(1, valid[r+1] - valid[r])
                answer += s * e
        return answer

    # based on Leetcode editorial
    # https://leetcode.com/problems/count-of-interesting-subarrays/editorial/?envType=daily-question&envId=2025-04-25
    # magic
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        n = len(nums)
        answer = 0
        # sum of valid indices up to current index
        prefix = 0
        # number of times a k valid indices (ie left bound)
        count = Counter([0])
        # increment through nums
        for i in range(n):
            # right bound increment valid indices
            prefix += nums[i] % modulo == k
            # find number of valid left bounds
            answer += count[(prefix - k + modulo) % modulo]
            # track this indices in valid left bounds
            count[prefix % modulo] += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,2,4]
        j = 2
        k = 1
        o = 3
        self.assertEqual(s.countInterestingSubarrays(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = [3,1,9,6]
        j = 3
        k = 0
        o = 2
        self.assertEqual(s.countInterestingSubarrays(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = [2,7]
        j = 7
        k = 0
        o = 1
        self.assertEqual(s.countInterestingSubarrays(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)