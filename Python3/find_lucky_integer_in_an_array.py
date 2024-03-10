# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of integers arr, a lucky integer is an integer that has a
    frequency in the array equal to its value.

    Return the largest lucky integer in the array. If there is no lucky integer
    return -1.
    '''
    def findLucky(self, arr: List[int]) -> int:
        a = -1
        c = Counter(arr)
        for i in c:
            if c[i] == i:
                a = max(a, i)
        return a

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,2,3,4]
        o = 2
        self.assertEqual(s.findLucky(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,2,3,3,3]
        o = 3
        self.assertEqual(s.findLucky(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)