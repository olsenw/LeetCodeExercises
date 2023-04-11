# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s, which contains starts *.

    In one operation:
    * Choose a star in s.
    * Remove the closest non-start character to its left, as well as the star
      itself.

    Return the string after all stars have been removed.

    Note:
    * The inputs are generated such that the operation is always possible.
    * It can be shown that the resulting string will always be unique.
    '''
    # uses a string as the stack
    def removeStars_passes(self, s: str) -> str:
        answer = ""
        for c in s:
            if c == '*':
                answer = answer[:-1]
            else:
                answer += c
        return answer

    def removeStars(self, s: str) -> str:
        a = []
        for c in s:
            if c == "*":
                a.pop()
            else:
                a.append(c)
        return ''.join(a)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "leet**cod*e"
        o = "lecoe"
        self.assertEqual(s.removeStars(i), o)

    def test_two(self):
        s = Solution()
        i = "erase*****"
        o = ""
        self.assertEqual(s.removeStars(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)