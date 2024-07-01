# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array arr, return true if there are three consecutive odd
    numbers in the array. Otherwise, return false.
    '''
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        answer = 0
        curr = 0
        for n in arr:
            if n % 2:
                curr += 1
            else:
                answer = max(answer, curr)
                curr = 0
        return max(answer,curr) >= 3

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,6,4,1]
        o = False
        self.assertEqual(s.threeConsecutiveOdds(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,34,3,4,5,7,23,12]
        o = True
        self.assertEqual(s.threeConsecutiveOdds(i), o)

    def test_three(self):
        s = Solution()
        i = [1,1,1]
        o = True
        self.assertEqual(s.threeConsecutiveOdds(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)