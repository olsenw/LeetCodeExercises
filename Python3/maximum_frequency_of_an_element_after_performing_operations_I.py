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
    * Select an index i that was not selected in any previous operations.
    * Add an integer in the range [-k, k] to nums[i].

    Return the maximum possible frequency of any element in num after performing
    the operations.
    '''
    # O(n^2)
    def maxFrequency_brute(self, nums: List[int], k: int, numOperations: int) -> int:
        answer = 0
        nums.sort()
        for i in range(nums[0], nums[-1] + 1):
            ans = 0
            ops = numOperations
            for n in nums:
                if n == i:
                    ans += 1
                elif ops and n-k <= i <= n+k:
                    ops -= 1
                    ans += 1
            answer = max(answer, ans)
        return answer

    # fancy version of brute force
    def maxFrequency_tle(self, nums: List[int], k: int, numOperations: int) -> int:
        answer = 0
        nums.sort()
        for i in range(nums[0], nums[-1] + 1):
            ans = 0
            ops = 0
            x = bisect.bisect_left(nums, i - k)
            y = bisect.bisect(nums, i + k)
            for j in range(x,y):
                if nums[j] == i:
                    ans += 1
                else:
                    ops += 1
            ans += min(ops, numOperations)
            answer = max(answer, ans)
        return answer

    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
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

    def test_three(self):
        s = Solution()
        i = [1,1,1,3,3,3]
        j = 1
        k = 6
        o = 6
        self.assertEqual(s.maxFrequency(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)