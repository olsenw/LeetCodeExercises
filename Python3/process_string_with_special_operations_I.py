# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s consisting of lowercase English letters and the special
    characters: *, #, and %.

    Build a new string result by processing s according to the following rules
    from left to right:
    * If the letter is a lowercase English letter append it to result.
    * A '*' removes the last character from result, if it exists.
    * A '#' duplicates the current result and appends it to itself.
    * A '%' reverses the current result.

    Return the final string result after processing all characters in s.
    '''
    def processStr(self, s: str) -> str:
        answer = ""
        for c in s:
            if c == '*':
                answer = answer[:-1]
            elif c == '#':
                answer += answer
            elif c == '%':
                answer = answer[::-1]
            else:
                answer += c
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "a#b%*"
        o = "ba"
        self.assertEqual(s.processStr(i), o)

    def test_two(self):
        s = Solution()
        i = "z*#"
        o = ""
        self.assertEqual(s.processStr(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)