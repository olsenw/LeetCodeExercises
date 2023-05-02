# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There is a function signFunc(x) that returns:
    * 1 if x is positive
    * -1 if x is negative
    * 0 if x is equal to 0

    Given an integer array nums. Let product be the product of all values in the
    array nums.

    Return signFunc(product).
    '''
    def arraySign(self, nums: List[int]) -> int:
        prod = 1
        for n in nums:
            prod *= n
            if prod == 0:
                return 0
        return -1 if prod < 0 else 1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [-1,-2,-3,-4,3,2,1]
        o = 1
        self.assertEqual(s.arraySign(i), o)

    def test_two(self):
        s = Solution()
        i = [1,5,0,2,-3]
        o = 0
        self.assertEqual(s.arraySign(i), o)

    def test_three(self):
        s = Solution()
        i = [-1,1,-1,1,-1]
        o = -1
        self.assertEqual(s.arraySign(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)