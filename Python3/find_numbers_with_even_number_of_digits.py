# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array nums of integers, return how many of them contain an even
    number of digits.
    '''
    def findNumbers(self, nums: List[int]) -> int:
        return sum(len(str(n)) % 2 == 0 for n in nums)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [12,345,2,6,7896]
        o = 2
        self.assertEqual(s.findNumbers(i), o)

    def test_two(self):
        s = Solution()
        i = [555,901,482,1771]
        o = 1
        self.assertEqual(s.findNumbers(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)