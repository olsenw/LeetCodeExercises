# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two integers, nums and t. A number x is achievable if it can become
    equal to num after applying the following operation at most t times.
    * Increase or decrease x by 1, and simultaneously increase or decrease num
      by 1.
    
    Return the maximum possible value of x.
    '''
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + 2 * t

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 4
        j = 1
        o = 6
        self.assertEqual(s.theMaximumAchievableX(i,j), o)

    def test_two(self):
        s = Solution()
        i = 3
        j = 2
        o = 7
        self.assertEqual(s.theMaximumAchievableX(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)