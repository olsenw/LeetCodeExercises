# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from math import gcd
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums, return the greatest common divisor of the
    smallest number and largest number in nums.

    The greatest common divisor of two numbers is the largest positive integer
    that evenly divides both numbers.
    '''
    def findGCD(self, nums: List[int]) -> int:
        a,b = min(nums), max(nums)
        # https://stackoverflow.com/questions/11175131/code-for-greatest-common-divisor-in-python
        # while b:
        #     a,b = b, a % b
        # return a
        return gcd(a,b)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,5,6,9,10]
        o = 2
        self.assertEqual(s.findGCD(i), o)

    def test_two(self):
        s = Solution()
        i = [7,5,6,8,3]
        o = 1
        self.assertEqual(s.findGCD(i), o)

    def test_two(self):
        s = Solution()
        i = [3,3]
        o = 3
        self.assertEqual(s.findGCD(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)