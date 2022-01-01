# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    # this has O(n^n) time... and O(n^n) space (lot of repeated work)
    def maxCoins_brute(self, nums: List[int]) -> int:
        best = 0
        def running(total, n: List[int]):
            if len(n) == 0:
                nonlocal best
                best = max(best, total)
                return
            for i in range(len(n)):
                r = n[i]
                if i - 1 >= 0: r *= n[i-1]
                if i + 1 < len(n): r *= n[i+1]
                running(total + r, n[0:i] + n[i+1:])
        running(0, nums)
        return best

    # based on answer from leetcode discussions
    # https://leetcode.com/problems/burst-balloons/discuss/1659214/Simple-GAP-Strategy-oror-DP-oror-Well-Explained
    def maxCoins_dp(self, nums: List[int]) -> int:
        # print("print")
        dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
        # move along the diagonal
        for limit in range(len(nums)):
            row = 0
            for col in range(limit, len(nums)):
                best = 0
                for index in range(row, col+1):
                    left = 0 if index == row else dp[row][index-1]
                    right = 0 if index == col else dp[index+1][col]
                    val = nums[index]
                    if row-1 >= 0: val *= nums[row-1]
                    if col+1 < len(nums): val *= nums[col+1]
                    best = max(best, left + val + right)
                dp[row][col] = best
                # print(dp, row, col, limit)
                row += 1
        # print(dp)
        return dp[0][-1]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,1,5,8]
        o = 167
        self.assertEqual(s.maxCoins_brute(i), o)
        self.assertEqual(s.maxCoins_dp(i), o)

    def test_two(self):
        s = Solution()
        i = [1,5]
        o = 10
        self.assertEqual(s.maxCoins_dp(i), o)
        self.assertEqual(s.maxCoins_brute(i), o)

    def test_three(self):
        s = Solution()
        i = [1,1]
        o = 2
        self.assertEqual(s.maxCoins_dp(i), o)
        self.assertEqual(s.maxCoins_brute(i), o)

    def test_four(self):
        s = Solution()
        i = [1,2,3,2,1]
        o = 12+4+2+2+2
        self.assertEqual(s.maxCoins_dp(i), o)
        self.assertEqual(s.maxCoins_brute(i), o)

    def test_five_dp(self):
        s = Solution()
        i = [1 for _ in range(500)]
        o = 500
        self.assertEqual(s.maxCoins_dp(i), o)
        # this takes too long
        # self.assertEqual(s.maxCoins_brute(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)