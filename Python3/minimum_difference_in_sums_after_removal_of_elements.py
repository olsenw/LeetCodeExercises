# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed integer array ums consisting of 3 * n elements.

    It is possible to remove any subsequence of elements of size exactly n from
    nums. The remaining 2 * n elements will be divided into two equal parts:
    * The first n elements belonging to the first part and their sum is
      sumfirst.
    * The next n elements belonging to the second part and their sum is
      sumsecond.
    
    The difference in sums of the two parts is denoted as sumfirst-sumsecond.

    Return the minimum difference possible between the sums of the two parts
    after the removal of n elements.
    '''
    def minimumDifference_brute(self, nums: List[int]) -> int:
        n = len(nums) // 3
        answer = float('inf')
        for i in range(n, 2*n+1):
            a = sum(sorted(nums[:i])[:n])
            b = sum(sorted(nums[i:],reverse=True)[:n])
            answer = min(answer, a - b)
        return answer

    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        answer = float('inf')
        # total = sum(nums)
        '''
        pre calc the minimum sum for end of array
        '''
        dp = dict()
        large = list(nums[2*n:])
        heapq.heapify(large)
        largeRunning = sum(nums[2*n:])
        dp[2*n] = largeRunning
        for i in range(2*n-1,n-1,-1):
            # b = sum(sorted(nums[i:],reverse=True)[:n])
            largeRunning += nums[i] - heapq.heappushpop(large, nums[i])
            dp[i] = largeRunning
            pass
        '''
        running smallest numbers for beginning of array
        '''
        # heap of the smallest elements
        small = [-i for i in nums[:n]]
        heapq.heapify(small)
        # running sum of the smallest elements
        smallRunning = sum(nums[:n])
        '''
        iterate all partition points
        '''
        for i in range(n, 2*n+1):
            # a = sum(sorted(nums[:i])[:n])
            # b = sum(sorted(nums[i:],reverse=True)[:n])
            answer = min(answer, smallRunning - dp[i])
            smallRunning += nums[i] + heapq.heappushpop(small, -nums[i])
            pass
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,1,2]
        o = -1
        self.assertEqual(s.minimumDifference(i), o)

    def test_two(self):
        s = Solution()
        i = [7,9,5,8,1,3]
        o = 1
        self.assertEqual(s.minimumDifference(i), o)

    def test_three(self):
        s = Solution()
        i = [1,6,3,44,22,1,3,2,1,3,66,7]
        o = -70
        self.assertEqual(s.minimumDifference(i), o)

    def test_four(self):
        s = Solution()
        i = [16,46,43,41,42,14,36,49,50,28,38,25,17,5,18,11,14,21,23,39,23]
        o = -14
        self.assertEqual(s.minimumDifference(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)