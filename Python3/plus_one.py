# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a large integer represented as an integer array digits, where each
    digits[i] is the ith digit of the integer. The digits are ordered from most
    significant to least significant in left-to-right order. The large integer
    does not contain any 0's.

    Increment the large integer by one and return the resulting array of digits.
    '''
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        index = len(digits) - 1
        while index > 0 and digits[index] > 9:
            digits[index] = 0
            digits[index - 1] += 1
            index -= 1
        if digits[0] > 9:
            digits[0] = 0
            return [1] + digits
        return digits

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3]
        o = [1,2,4]
        self.assertEqual(s.plusOne(i), o)

    def test_two(self):
        s = Solution()
        i = [4,3,2,1]
        o = [4,3,2,2]
        self.assertEqual(s.plusOne(i), o)

    def test_three(self):
        s = Solution()
        i = [9]
        o = [1,0]
        self.assertEqual(s.plusOne(i), o)

    # invalid test case due to leading zero
    def test_four(self):
        s = Solution()
        i = [0,0,9]
        o = [0,1,0]
        self.assertEqual(s.plusOne(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)