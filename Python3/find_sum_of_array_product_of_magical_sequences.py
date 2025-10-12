# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two integers, m and k, and an integer array nums.

    A sequence of integers seq is called magical if:
    * seq has a size of m.
    * 0 <= seq[i] < nums.length
    * The binary representation of 2 ^ seq[0] + 2 ^ seq[1] + ... + 2 ^ seq[m-1]
      has k set bits.
    
    The array product of this sequence is defined as
    prod(seq) = (nums[seq[0]] * nums[seq[1]] * ... * nums[seq[m-1]]).

    Return the sum of the array products for all valid magical sequences.

    Since the answer may be large, return it modulo 10^9 + 7.

    A set bit refers to a bit in the binary representation of a number that has
    a value of 1.
    '''
    # based on Leetcode editorial
    # https://leetcode.com/problems/find-sum-of-array-product-of-magical-sequences/editorial/?envType=daily-question&envId=2025-10-12
    # lot of voodoo magic
    # a lot of precalculation happens
    # a big dp table is created
    # answer is derived from valid entries in dp table
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        n = len(nums)
        mod = 10 ** 9 + 7

        def quickmul(x:int, y:int) -> int:
            res, cur = 1, x % mod
            while y:
                if y & 1:
                    res = res * cur % mod
                y >>= 1
                cur = cur * cur % mod
            return res

        fac = [1] * (m + 1)
        for i in range(1, m + 1):
            fac[i] = fac[i - 1] * i % mod
        
        ifac = [1] * (m + 1)
        for i in range(2, m + 1):
            ifac[i] = quickmul(i, mod - 2)
        for i in range(2, m + 1):
            ifac[i] = ifac[i-1] * ifac[i] % mod
        
        numsPower = [[1] * (m + 1) for _ in range(n)]
        for i in range(n):
            for j in range(1, m + 1):
                numsPower[i][j] = numsPower[i][j-1] * nums[i] % mod
        
        f = [
            [[[0] * (k+1) for _ in range(m * 2 + 1)] for _ in range(m + 1)]
            for _ in range(n)
        ]

        for j in range(m + 1):
            f[0][j][j][0] = numsPower[0][j] * ifac[j] % mod
        
        for i in range(n - 1):
            for j in range(m + 1):
                for p in range(m * 2 + 1):
                    for q in range(k + 1):
                        if f[i][j][p][q] == 0:
                            continue
                        q2 = (p % 2) + q
                        if q2 > k:
                            break
                        for r in range(m-j+1):
                            p2 = (p//2) + r
                            if p2 > m * 2:
                                continue
                            f[i+1][j+r][p2][q2] = (
                                f[i+1][j+r][p2][q2]
                                + f[i][j][p][q]
                                * numsPower[i+1][r]
                                % mod
                                * ifac[r]
                                % mod
                            ) % mod
        
        res = 0
        for p in range(m*2+1):
            for q in range(k+1):
                if bin(p).count("1") + q == k:
                    res = (res + f[n-1][m][p][q] * fac[m] % mod) % mod
        return res

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 5
        j = 5
        k = [1,10,100,10000,1000000]
        o = 991600007
        self.assertEqual(s.magicalSum(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = 2
        j = 2
        k = [5,4,3,2,1]
        o = 170
        self.assertEqual(s.magicalSum(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = 1
        j = 1
        k = [28]
        o = 28
        self.assertEqual(s.magicalSum(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)