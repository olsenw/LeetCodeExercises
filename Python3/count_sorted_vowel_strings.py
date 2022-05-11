# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an integer n, return the number of strings of length n that
    consist only of vowels (a, e, i, o, u) and are lexicographically
    sorted.

    A string s is lexicographically sorted if for all valid i, s[i] is
    the same as or comes before s[i+1] in the alphabet.
    '''
    def countVowelStrings(self, n: int) -> int:
        # count of strings that end in letter (a,e,i,o,u)
        dp = [1,1,1,1,1]
        for _ in range(n-1):
            u = list(dp)
            for v in range(5):
                u[v] += sum(dp[:v])
            dp = u
        return sum(dp)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 1
        o = 5
        self.assertEqual(s.countVowelStrings(i), o)

    def test_two(self):
        s = Solution()
        i = 2
        o = 15
        self.assertEqual(s.countVowelStrings(i), o)

    def test_three(self):
        s = Solution()
        i = 33
        o = 66045
        self.assertEqual(s.countVowelStrings(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)