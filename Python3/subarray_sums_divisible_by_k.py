# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from itertools import accumulate
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an integer array nums and an integer k, return the number of non-empty
    subarrays that have a sum divisible by k.
    '''
    # O(n^2) time 66/73 test cases
    def subarraysDivByK_tle(self, nums: List[int], k: int) -> int:
        answer = 0
        prefix = [0] + list(accumulate(nums))
        for i in range(1, len(prefix)):
            for j in range(i - 1, -1, -1):
                if (prefix[i] - prefix[j]) % k == 0:
                    answer += 1
        return answer

    # based on Leetcode solution
    # https://leetcode.com/problems/subarray-sums-divisible-by-k/solutions/2913063/subarray-sums-divisible-by-k/?orderBy=most_votes
    # O(n + k) time and O(k) space
    # smart math... not sure what doing 
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        answer = 0
        # store running total remainder
        prefixMod = 0
        # number subarrays with remainder R
        modGroups = [0] * k
        modGroups[0] = 1
        # iterate over array
        for i in range(len(nums)):
            # running prefix (uses trick to cancel out negative numbers)
            prefixMod = (prefixMod + nums[i] % k + k) % k
            # update answer
            answer += modGroups[prefixMod]
            # updated subarrays with this mod
            modGroups[prefixMod] += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [4,5,0,-2,-3,1]
        j = 5
        o = 7
        self.assertEqual(s.subarraysDivByK(i,j), o)

    def test_two(self):
        s = Solution()
        i = [5]
        j = 9
        o = 0
        self.assertEqual(s.subarraysDivByK(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)