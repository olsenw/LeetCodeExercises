# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums with the following properties:
    * nums.length == 2 * n
    * nums contains n + 1 unique elements
    * Exactly one element that is repeated n times.

    Return the element that is repeated n times.
    '''
    def repeatedNTimes(self, nums: List[int]) -> int:
        s = set()
        for n in nums:
            if n in s:
                return n
            s.add(n)
        return None

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,3]
        o = 3
        self.assertEqual(s.repeatedNTimes(i), o)

    def test_two(self):
        s = Solution()
        i = [2,1,2,5,3,2]
        o = 2
        self.assertEqual(s.repeatedNTimes(i), o)

    def test_three(self):
        s = Solution()
        i = [5,1,5,2,5,3,5,4]
        o = 5
        self.assertEqual(s.repeatedNTimes(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)