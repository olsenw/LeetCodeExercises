# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a positive integer n, find the pivot integer such that:
    * The sum of all elements between 1 and x inclusively equals the sum of all
      elements between x and n inclusively.
    
    Return the pivot integer x if no such integer exists, return -1. It is
    guaranteed that there will be at most one pivot index for the given input.
    '''
    def pivotInteger(self, n: int) -> int:
        x,y = 0, n * (n + 1) // 2
        for i in range(1,n+1):
            x += i
            if x == y:
                return i
            y -= i
        return -1

    '''
    Could probably use binary search if search space was larger.
    '''
class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 8
        o = 6
        self.assertEqual(s.pivotInteger(i), o)

    def test_two(self):
        s = Solution()
        i = 1
        o = 1
        self.assertEqual(s.pivotInteger(i), o)

    def test_three(self):
        s = Solution()
        i = 4
        o = -1
        self.assertEqual(s.pivotInteger(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)