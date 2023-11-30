# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer n, transform it into 0 using the following operations any
    number of times:
    * Change the rightmost (0th) bit in the binary representation of n.
    * Change the ith bit in the binary representation of n if the (i-1)th bit is
      set to 1 and the (i-2)th through oth bits are set to 0.
    
    Return the minimum number of operations to transform n into 0.
    '''
    # based on LeetCode solution
    # https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/editorial/?envType=daily-question&envId=2023-11-30
    # this is wack magic
    def minimumOneBitOperations(self, n: int) -> int:
        # base case everything is zero
        if n == 0:
            return 0
        k = 0
        c = 1 # represents 2^k
        while c * 2 <= n:
            c *= 2
            k += 1
        return 2**(k + 1) - 1 - self.minimumOneBitOperations(n ^ c)

    # tricky
    # https://en.wikipedia.org/wiki/Gray_code
    def minimumOneBitOperations_GrayCode(self, n: int) -> int:
        ans = n
        ans ^= ans >> 16
        ans ^= ans >> 8
        ans ^= ans >> 4
        ans ^= ans >> 2
        ans ^= ans >> 1
        return ans

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 3
        o = 2
        self.assertEqual(s.minimumOneBitOperations(i), o)

    def test_two(self):
        s = Solution()
        i = 6
        o = 4
        self.assertEqual(s.minimumOneBitOperations(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)