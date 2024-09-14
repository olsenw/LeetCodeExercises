# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums of size n.

    Consider a non-empty subarray from nums that has the maximum possible
    bitwise AND.

    Return the length of the longest such subarray.

    The bitwise AND of an array is the bitwise AND of all the numbers in it.

    A subarray is a contiguous sequence of elements within an array.
    '''
    def longestSubarray(self, nums: List[int]) -> int:
        a,b,c = 0,0,0
        for n in nums:
            if n > a:
                a,b,c = n,1,1
            elif n == a:
                b += 1
            else:
                c = max(b,c)
                b = 0
        return max(b,c)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,3,2,2]
        o = 2
        self.assertEqual(s.longestSubarray(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,4]
        o = 1
        self.assertEqual(s.longestSubarray(i), o)

    def test_three(self):
        s = Solution()
        i = [378034,378034,378034]
        o = 3
        self.assertEqual(s.longestSubarray(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)