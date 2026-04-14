# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums and an integer digit.

    Return the total number of times digit appears in the decimal
    representation of all elements in nums.
    '''
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        answer = 0
        digit = str(digit)
        for n in nums:
            answer += str(n).count(digit)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [12,54,32,22]
        j = 2
        o = 4
        self.assertEqual(s.countDigitOccurrences(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,34,7]
        j = 9
        o = 0
        self.assertEqual(s.countDigitOccurrences(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)