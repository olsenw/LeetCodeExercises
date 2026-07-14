# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import math
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums.

    Find the number of pairs of non-empty subsequences (seq1, seq2) of nums that
    satisfy the following conditions:
    * The subsequence seq1 and seq2 are disjoint meaning no index of nums is
      common between them.
    * The GCD of the elements of seq1 is equal to the GCD of the elements of
      seq2.
    
    Return the total number of such pairs.

    Since the answer may be very large, return it modulo 10^9 + 7.
    '''
    # Based on leetcode editorial
    # https://leetcode.com/problems/find-the-number-of-subsequences-with-equal-gcd/?envType=daily-question&envId=2026-07-14
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        # find upper bound for GCD (GCD can never be larger than biggest element)
        m = max(nums)
        # dp array where GCD of first subsequence is j and GCD of second subsequence is k
        # will be updated over each index (reduces size of dp array)
        dp = [[0] * (m + 1) for _ in range(m + 1)]
        dp[0][0] = 1

        for num in nums:
            newDP = [[0] * (m + 1) for _ in range(m + 1)]
            for j in range(m + 1):
                divisorA = math.gcd(j, num)
                for k in range(m + 1):
                    value = dp[j][k]
                    # GCD already 0 no point updating
                    if value == 0:
                        continue
                    divisorB = math.gcd(k, num)
                    # not added to either sequence
                    newDP[j][k] = (newDP[j][k] + value) % MOD
                    # sequence nums[i] added to first sequence
                    newDP[divisorA][k] = (newDP[divisorA][k] + value) % MOD
                    # sequence nums[i] added to second sequence
                    newDP[j][divisorB] = (newDP[j][divisorB] + value) % MOD
            dp = newDP
        
        # find all values where the two subsequence GCD are equal
        answer = 0
        for j in range(1, m + 1):
            answer = (answer + dp[j][j]) % MOD
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,4]
        o = 10
        self.assertEqual(s.subsequencePairCount(i), o)

    def test_two(self):
        s = Solution()
        i = [10,20,30]
        o = 2
        self.assertEqual(s.subsequencePairCount(i), o)

    def test_three(self):
        s = Solution()
        i = [1,1,1,1]
        o = 50
        self.assertEqual(s.subsequencePairCount(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)