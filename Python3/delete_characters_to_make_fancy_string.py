# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A fancy string is a string where no three consecutive characters are equal.

    Given a string s, delete the minimum possible number of character from s to
    make it fancy.

    Return the final string after the deletion. It can be shown that the answer
    will always be unique.
    '''
    def makeFancyString(self, s: str) -> str:
        return s[:2] + ''.join(c for i,c in enumerate(s[2:], 2) if not (c == s[i-1] and c == s[i-2]))
        # answer = list(s[:2])
        # for i in range(2, len(s)):
        #     if not (s[i] == s[i-1] and s[i] == s[i-2]):
        #         answer.append(s[i])
        # return ''.join(answer)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "leeetcode"
        o = "leetcode"
        self.assertEqual(s.makeFancyString(i), o)

    def test_two(self):
        s = Solution()
        i = "aaabaaaa"
        o = "aabaa"
        self.assertEqual(s.makeFancyString(i), o)

    def test_three(self):
        s = Solution()
        i = "aab"
        o = "aab"
        self.assertEqual(s.makeFancyString(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)