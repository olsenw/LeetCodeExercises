# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of positive integers nums, and a positive integer k.

    An operation can be preformed once on nums, where any non-overlapping prefix
    and suffix from nums can be removed such that nums remains non-empty.

    Find the x-value of nums. which is the number of ways to preform this
    operation so that the product of the remaining elements leaves a remainder
    of x when divided by k.

    Return an array result of size k where result[x] is the x-value of nums for
    0 <= x <= k - 1.

    A prefix of an array is a subarray that starts from the beginning of the
    array and extends to any point within it.

    A suffix of an array is a subarray that stats at any point within the array
    and extends to the end of the array.

    Note that the prefix and suffix to be chosen for the operation can be empty.
    '''
    def resultArray_incomplete(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        prefix = [nums[0] % k] * n
        suffix = [nums[-1] % k] * n
        for i in range(1,n):
            prefix[i] = (prefix[i-1] * nums[i] % k) % k
            suffix[n-i-1] = (suffix[n-i] + nums[n-i-1] % k) % k
        return

    # attempt at following hints (but math really wrong)
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        dp = [[0]*k for _ in range(n)]
        dp[0][nums[0] % k] = 1
        for i in range(1,n):
            dp[i][nums[i]%k] += 1
            for j in range(k):
                r = (nums[i] % k * j) % k
                dp[i][r] += dp[i-1][j]
        return [sum(dp[i][j] for i in range(n)) for j in range(k)]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,4,5]
        j = 3
        o = [9,2,4]
        self.assertEqual(s.resultArray(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,2,4,8,16,32]
        j = 4
        o = [18,1,2,0]
        self.assertEqual(s.resultArray(i,j), o)

    def test_three(self):
        s = Solution()
        i = [1,1,2,1,1]
        j = 2
        o = [9,6]
        self.assertEqual(s.resultArray(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)