# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict
from functools import cache
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

from sortedcontainers import SortedList

class Solution:
    '''
    Given an integer array nums and two integers x and k. The following
    operation can be preformed any number of times (including zero):
    * Increase or decrease any element of nums by 1.

    Return the minimum number of operations needed to have at least k
    non-overlapping subarrays of size exactly x in nums, where all elements
    within each subarray are equal.
    '''
    # runs in O(n^2) time
    # see precalc for loop with embedded sum
    # use of sorted list also probably a problem
    def minOperations_tle(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        l = SortedList(nums[:x-1])
        s = sum(nums[:x-1])
        # medians = []
        # sums = []
        operations = []
        for i in range(x-1,n):
            l.add(nums[i])
            s += nums[i]
            if x % 2 == 1:
                median = l[(x) // 2]
            else:
                median = (l[x//2-1] + l[x//2]) // 2
            # medians.append(median)
            # sums.append(s)
            # bad because O(n^2)
            o = sum(abs(m - median) for m in l)
            operations.append(o)
            l.remove(nums[i-x+1])
            s -= nums[i-x+1]
        @cache
        def dp(i:int,r:int) -> int:
            if r == 0:
                return 0
            if i >= len(operations):
                return float('inf')
            a = operations[i] + dp(i+x, r-1)
            b = dp(i+1,r)
            return min(a,b)
        return dp(0,k)

    # does not correctly count operations in precalc phase
    def minOperations_fails(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        l = SortedList(nums[:x-1])
        posSum = 0
        posCount = 0
        negSum = 0
        negCount = 0
        for i in nums[:x-1]:
            if i >= 0:
                posSum += i
                posCount += 1
            else:
                negSum -= i
                negCount += 1
        operations = []
        for i in range(x-1,n):
            l.add(nums[i])
            if nums[i] >= 0:
                posSum += nums[i]
                posCount += 1
            else:
                negSum -= nums[i]
                negCount += 1
            if x % 2 == 1:
                median = l[(x) // 2]
            else:
                median = (l[x//2-1] + l[x//2]) // 2
            posOps = abs(median * posCount - posSum)
            negOps = median * negCount + negSum
            operations.append(posOps + negOps)
            l.remove(nums[i-x+1])
            if nums[i-x+1] >= 0:
                posSum -= nums[i-x+1]
                posCount -= 1
            else:
                negSum += nums[i-x+1]
                negCount -= 1
        @cache
        def dp(i:int,r:int) -> int:
            if r == 0:
                return 0
            if i >= len(operations):
                return float('inf')
            a = operations[i] + dp(i+x, r-1)
            b = dp(i+1,r)
            return min(a,b)
        return dp(0,k)

    # based on LeetCode editorial
    # https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/editorial/?envType=daily-question&envId=2026-11-04
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        left,right = [],[]
        delayed = defaultdict(int)
        leftSize = rightSize = 0
        leftSum = rightSum = 0
        operations = [0] * n
        def prune(heap:List[int],sign:int) -> None:
            while heap and delayed[sign * heap[0]]:
                delayed[sign * heap[0]] -= 1
                heapq.heappop(heap)
        def balance() -> None:
            nonlocal leftSize,rightSize,leftSum,rightSum
            if leftSize > rightSize + 1:
                num = -heapq.heappop(left)
                heapq.heappush(right, num)
                leftSum -= num
                rightSum += num
                leftSize -= 1
                rightSize += 1
                prune(left, -1)
            elif rightSize > leftSize:
                num = heapq.heappop(right)
                heapq.heappush(left, -num)
                leftSum += num
                rightSum -= num
                leftSize += 1
                rightSize -= 1
                prune(right, 1)
        for i, num in enumerate(nums):
            if not left or num <= -left[0]:
                heapq.heappush(left, -num)
                leftSize += 1
                leftSum += num
            else:
                heapq.heappush(right, num)
                rightSize += 1
                rightSum += num
            balance()
            if i >= x:
                num = nums[i-x]
                delayed[num] += 1
                if num <= -left[0]:
                    leftSize -= 1
                    leftSum -= num
                    if num == -left[0]:
                        prune(left, -1)
                else:
                    rightSize -= 1
                    rightSum -= num
                    if num == right[0]:
                        prune(right, 1)
                balance()
            if i >= x - 1:
                mid = -left[0]
                operations[i] = rightSum - leftSum + mid * (leftSize - rightSize)
        # causes memory to be exceeded
        # @cache
        # def dp(i:int,r:int) -> int:
        #     if r == 0:
        #         return 0
        #     if i >= len(operations):
        #         return float('inf')
        #     a = operations[i] + dp(i+x, r-1)
        #     b = dp(i+1,r)
        #     return min(a,b)
        # dp.cache_clear()
        # return dp(x-1,k)
        dp = [[0] + [float('inf')] * k for _ in range(n)]
        for j in range(1, k + 1):
            if j == 1:
                dp[x - 1][j] = operations[x - 1]
            else:
                dp[j * x - 1][j] = dp[(j - 1) * x - 1][j - 1] + operations[j * x - 1]
        for j in range(1, k + 1):
            for i in range(j * x, n):
                dp[i][j] = min(dp[i - x][j - 1] + operations[i], dp[i - 1][j])
        return dp[n - 1][k]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [5,-2,1,3,7,3,6,4,-1]
        j = 3
        k = 2
        o = 8
        self.assertEqual(s.minOperations(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = [9,-2,-2,-2,1,5]
        j = 2
        k = 2
        o = 3
        self.assertEqual(s.minOperations(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)