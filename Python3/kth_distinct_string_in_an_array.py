# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    A distinct string is a string that is present only once in an array.

    Given an array of strings arr, and an integer k, return the kth distinct
    string present in arr. If there are fewer than k distinct strings, return an
    empty string "".

    Note that the strings are considered in the order in which they appear in
    the array.
    '''
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c = Counter(arr)
        for s in arr:
            if c[s] == 1: 
                if  k == 1:
                    return s
                k -= 1
        return ""

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["d","b","c","b","c","a"], 2
        o = "a"
        self.assertEqual(s.kthDistinct(*i), o)

    def test_two(self):
        s = Solution()
        i = ["aaa","aa","a"], 1
        o = "aaa"
        self.assertEqual(s.kthDistinct(*i), o)

    def test_three(self):
        s = Solution()
        i = ["a","b","a"], 3
        o = ""
        self.assertEqual(s.kthDistinct(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)