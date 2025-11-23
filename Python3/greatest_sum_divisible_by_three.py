# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums, return the maximum possible sum of elements of
    the array such that it is divisible by three.
    '''
    def maxSumDivThree_fail(self, nums: List[int]) -> int:
        one = []
        two = []
        answer = 0
        for n in nums:
            if n % 3 == 1:
                one.append(n)
            elif n % 3 == 2:
                two.append(n)
            else:
                answer += n
        one.sort(reverse=True)
        two.sort(reverse=True)
        l = min(len(one), len(two))
        return answer + sum(one[:l]) + sum(two[:l])

    def maxSumDivThree_fails(self, nums: List[int]) -> int:
        def dp(i:int, mod:int) -> int:
            if i == len(nums):
                return 0
            n = nums[i]
            m = (n % 3 + mod) % 3
            a = dp(i + 1, mod)
            b = n + dp(i + 1, m)
            if b % 3 != mod:
                b = 0
            return max(a,b)
        return dp(0,0)

    def maxSumDivThree_incomplete(self, nums: List[int]) -> int:
        dp = [[0] * 3 for _ in range(len(nums)+1)]
        for i in range(len(nums)-1,-1,-1):
            n = nums[i]
            m = n % 3
        return
    
    def maxSumDivThree_fails(self, nums: List[int]) -> int:
        mods = [[] for _ in range(3)]
        for n in nums:
            mods[n % 3].append(n)
        for i in range(3):
            mods[i].sort(reverse=True)
        def dp(s:int, i:int, j:int):
            if i == len(mods[1]):
                return 0
            a,b = 0,0
            if i < len(mods[1]) - 3:
                a = dp(s + sum(mods[1][i:i+3]), i + 3, j)
            if j < len(mods[2]):
                b = dp(s + mods[1][i] + mods[2][j], i + 1, j + 1)
            return max(a,b)
        answer = sum(mods[0]) + dp(0,0,0)
        return answer

    def maxSumDivThree_fails(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * 3 for _ in range(n)]
        dp[0][nums[0] % 3] = nums[0]
        for i in range(1,n):
            m = nums[i] % 3
            dp[i][m % 3] = nums[i]
            for j in range(3):
                k = (3 - m + j) % 3
                dp[i][j] += dp[i-1][k]
        return dp[n-1][0]

    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * 3 for _ in range(n)]
        dp[0][nums[0] % 3] = nums[0]
        for i in range(1,n):
            for j in range(3):
                dp[i][j] = max(dp[i][j], dp[i-1][j])
                x = dp[i-1][j] + nums[i]
                y = x % 3
                dp[i][y] = max(dp[i][y], x)
        return dp[n-1][0]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,6,5,1,8]
        o = 18
        self.assertEqual(s.maxSumDivThree(i), o)

    def test_two(self):
        s = Solution()
        i = [4]
        o = 0
        self.assertEqual(s.maxSumDivThree(i), o)

    def test_three(self):
        s = Solution()
        i = [1,2,3,4,4]
        o = 12
        self.assertEqual(s.maxSumDivThree(i), o)

    def test_four(self):
        s = Solution()
        i = [1,2]
        o = 3
        self.assertEqual(s.maxSumDivThree(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)