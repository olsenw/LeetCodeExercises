# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    An array is considered special if every pair of its adjacent elements
    contains two numbers with different parity.

    Given an array of integers nums. Return true if nums is a special array,
    otherwise, return false.
    '''
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        p = nums[0] % 2
        for n in nums[1:]:
            t = n % 2
            if p == t:
                return False
            p = t
        return True

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1]
        o = True
        self.assertEqual(s.isArraySpecial(i), o)

    def test_two(self):
        s = Solution()
        i = [2,1,4]
        o = True
        self.assertEqual(s.isArraySpecial(i), o)

    def test_three(self):
        s = Solution()
        i = [4,3,1,6]
        o = False
        self.assertEqual(s.isArraySpecial(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)