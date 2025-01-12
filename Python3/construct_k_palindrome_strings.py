# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    Given a string s and an integer k, return true if it is possible to
    construct k palindrome strings using all the letters or false otherwise.
    '''
    # based on hints (give away the problem)
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        c = Counter(s)
        odd = []
        even = []
        for i in c:
            if c[i] % 2:
                odd.append(c[i])
            else:
                even.append(c[i])
        if len(odd) > k:
            return False
        return True

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "annabelle"
        j = 2
        o = True
        self.assertEqual(s.canConstruct(i,j), o)

    def test_two(self):
        s = Solution()
        i = "leetcode"
        j = 3
        o = False
        self.assertEqual(s.canConstruct(i,j), o)

    def test_three(self):
        s = Solution()
        i = "true"
        j = 4
        o = True
        self.assertEqual(s.canConstruct(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)