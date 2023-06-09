# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from bisect import bisect
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of characters letters that is sorted in non-decreasing order,
    and a character target. There are at least two different characters in
    letters.

    Return the smallest character in letters that is lexicographically greater
    than target. If such a character does not exist, return the first character
    in letters.
    '''
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        i,j = 0, len(letters) - 1
        while i <= j:
            k = (i + j) // 2
            if letters[k] <= target:
                i = k + 1
            else:
                j = k - 1
        return letters[i] if i < len(letters) else letters[0]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["c","f","j"]
        j = "a"
        o = "c"
        self.assertEqual(s.nextGreatestLetter(i,j), o)

    def test_two(self):
        s = Solution()
        i = ["c","f","j"]
        j = "c"
        o = "f"
        self.assertEqual(s.nextGreatestLetter(i,j), o)

    def test_three(self):
        s = Solution()
        i = ["c","f","j"]
        j = "i"
        o = "j"
        self.assertEqual(s.nextGreatestLetter(i,j), o)

    def test_four(self):
        s = Solution()
        i = ["c","f","j"]
        j = "j"
        o = "c"
        self.assertEqual(s.nextGreatestLetter(i,j), o)

    def test_five(self):
        s = Solution()
        i = ["x","x","y","y"]
        j = "z"
        o = "x"
        self.assertEqual(s.nextGreatestLetter(i,j), o)

    def test_six(self):
        s = Solution()
        i = ["x","x","y","y"]
        j = "x"
        o = "y"
        self.assertEqual(s.nextGreatestLetter(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)