# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed integer array nums and a positive integer k.

    The following operation may be preformed any number of times:
    * Choose any two distinct indices i and j and simultaneously update the
      values of nums[i] to (nums[i] AND nums[j]) and nums[j] to
      (nums[i] OR nums[j]). Here, OR denotes the bitwise OR operation, and AND
      denotes the bitwise AND operation.
    
    Choose k elements from the final array and calculate the sum of their
    squares.

    Return the maximum sum of squares that can be achieved.

    Since the answer can be very large, return it modulo 10**9 + 7.
    '''
    # passes 913/918
    def maxSum_tle(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        for i in range(k):
            a = nums[i]
            for j in range(len(nums)-1,i,-1):
                b = nums[j]
                if a | b > a:
                    nums[i] = a | b
                    nums[j] = a & b
                    a = a | b
        return sum(n * n for n in nums[:k]) % (10**9 + 7)

    # based on Leetcode editorial
    # https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares/editorial/?envType=daily-question&envId=2026-10-12
    # the operation moves 1bits to final number
    # track what bits are available, and then build numbers from those bits
    def maxSum(self, nums: List[int], k: int) -> int:
        bits = 32
        # number of bits at a given binary position
        c = [0] * bits
        for n in nums:
            for i in range(32):
                if n & (1 << i):
                    c[i] += 1
        answer = 0
        for _ in range(k):
            m = 1 << (bits - 1)
            a = 0
            for i in range(bits-1,-1,-1):
                if c[i]:
                    a |= m
                    c[i] -= 1
                m >>= 1
            answer += a * a
        return answer % (10**9 + 7)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,6,5,8]
        j = 2
        o = 261
        self.assertEqual(s.maxSum(i,j), o)

    def test_two(self):
        s = Solution()
        i = [4,5,4,7]
        j = 3
        o = 90
        self.assertEqual(s.maxSum(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)