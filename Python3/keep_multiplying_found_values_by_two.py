# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of integers nums. Also given an integer original which is the
    first number that needs to be searched for in nums.

    Then perform the following steps:
    1) If original is found in nums, multiple it by two.
    2) Otherwise, stop the process.
    3) Repeat this process with the number as long as the number keeps being
       found.
    
    Return the final value of original.
    '''
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums = set(nums)
        while original in nums:
            original *= 2
        return original

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [5,3,6,1,12]
        j = 3
        o = 24
        self.assertEqual(s.findFinalValue(i,j), o)

    def test_two(self):
        s = Solution()
        i = [2,7,9]
        j = 4
        o = 4
        self.assertEqual(s.findFinalValue(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)