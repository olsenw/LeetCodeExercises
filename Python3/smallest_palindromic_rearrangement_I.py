# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        c = Counter(s)
        center = ""
        answer = ""
        for k in sorted(c.keys()):
            d,r = divmod(c[k],2)
            if d > 0:
                answer += k * d
            if r == 1:
                center = k
        answer += center
        for k in sorted(c.keys(), reverse=True):
            d,r = divmod(c[k],2)
            if d > 0:
                answer += k * d
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "z"
        o = "z"
        self.assertEqual(s.smallestPalindrome(i), o)

    def test_two(self):
        s = Solution()
        i = "babab"
        o = "abbba"
        self.assertEqual(s.smallestPalindrome(i), o)

    def test_three(self):
        s = Solution()
        i = "babab"
        o = "abbba"
        self.assertEqual(s.smallestPalindrome(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)