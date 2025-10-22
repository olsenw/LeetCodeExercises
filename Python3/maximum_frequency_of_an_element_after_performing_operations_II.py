# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import bisect
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums and two integers k and numOperations.

    Perform an operation numOperations times on nums, where in each operation:
    * Select an index i that was not selected in any previous operations
    * Add an integer in the range [-k,k] to nums[i].

    Return the maximum possible frequency of any element in nums after
    performing the operations.
    '''
    # solution to yesterday's problem
    # results in a tle
    # this is because answer search space is bigger (10^9 vs 10^5)
    def maxFrequency_tle(self, nums: List[int], k: int, numOperations: int) -> int:
        answer = 0
        nums.sort()
        i,j = 0,0
        # try every possible answer
        for n in range(nums[0], nums[-1] + 1):
            pass
            # do sliding window
            while nums[i] < n - k:
                i += 1
            while j < len(nums) and nums[j] <= n + k:
                j += 1
            a = bisect.bisect_left(nums, n)
            b = bisect.bisect(nums, n)
            actual = b - a
            ops = j - i - actual
            answer = max(answer, actual + min(numOperations, ops))
        return answer

    # hint is huge help!
    # for any given n in num, only three possible answers for most frequent
    # element: num[i] - k, num[i], num[i] + k
    # makes search space 3 * 10^5
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        answer = 0
        nums.sort()
        test = set()
        for n in nums:
            test.add(n - k)
            test.add(n)
            test.add(n + k)
        i,j = 0,0
        # try every possible answer
        for n in sorted(test):
            pass
            # do sliding window
            while nums[i] < n - k:
                i += 1
            while j < len(nums) and nums[j] <= n + k:
                j += 1
            a = bisect.bisect_left(nums, n)
            b = bisect.bisect(nums, n)
            actual = b - a
            ops = j - i - actual
            answer = max(answer, actual + min(numOperations, ops))
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,4,5]
        j = 1
        k = 2
        o = 2
        self.assertEqual(s.maxFrequency(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = [5,11,20,20]
        j = 5
        k = 1
        o = 2
        self.assertEqual(s.maxFrequency(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)