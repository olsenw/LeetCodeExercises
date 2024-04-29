# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import reduce
from itertools import accumulate
from operator import xor
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed integer array nums and a positive integer k.

    The following operation can be applied to the array any number of times:
    * Choose any element of the array and flip a bit in its binary
      representation. Flipping a bit means changing a 0 to 1 or vice versa.
    
    Return the minimum number of operations required to make the bitwise XOR of
    all elements of the final array equal to k.

    Note that the leading zero bits can be flipped in binary representation
    elements.
    '''
    def minOperations(self, nums: List[int], k: int) -> int:
        return bin(reduce(xor, nums) ^ k)[2:].count('1')

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,1,3,4]
        j = 1
        o = 2
        self.assertEqual(s.minOperations(i,j), o)

    def test_two(self):
        s = Solution()
        i = [2,0,2,0]
        j = 0
        o = 0
        self.assertEqual(s.minOperations(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)