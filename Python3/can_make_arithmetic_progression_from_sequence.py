# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A sequence of numbers is called an arithmetic progression if the difference
    between any two consecutive elements is the same.

    Given an array of numbers arr, return true if the array can be rearranged to
    form an arithmetic progression. Otherwise, return falls.
    '''
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        target = arr[1] - arr[0]
        for i in range(2,len(arr)):
            if arr[i] - arr[i-1] != target:
                return False
        return True

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,5,1]
        o = True
        self.assertEqual(s.canMakeArithmeticProgression(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,4]
        o = False
        self.assertEqual(s.canMakeArithmeticProgression(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)