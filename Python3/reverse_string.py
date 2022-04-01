# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Write a function that reverses a string. The input string is given
    as an array of characters s.

    Modify the input array in-place with O(1) space.
    '''
    # spirit of the problem
    def reverseString(self, s: List[str]) -> None:
        i = 0
        j = len(s) - 1
        while i <= j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

    # way faster
    def reverseString_alt(self, s: List[str]) -> None:
        s.reverse()

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["h","e","l","l","o"]
        o = ["o","l","l","e","h"]
        s.reverseString(i)
        self.assertEqual(i, o)
        i = ["h","e","l","l","o"]
        s.reverseString_alt(i)
        self.assertEqual(i, o)

    def test_two(self):
        s = Solution()
        i = ["H","a","n","n","a","h"]
        o = ["h","a","n","n","a","H"]
        s.reverseString(i)
        self.assertEqual(i, o)
        i = ["H","a","n","n","a","h"]
        s.reverseString_alt(i)
        self.assertEqual(i, o)

if __name__ == '__main__':
    unittest.main(verbosity=2)