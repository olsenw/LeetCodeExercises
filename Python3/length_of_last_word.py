# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s consisting of words and spaces, return the length of the
    last word in the string.
    
    A word is a maximal substring consisting of non-space characters only.
    '''
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while s[i] == ' ':
            i -= 1
        answer = 0
        while i > -1 and s[i] != ' ':
            answer += 1
            i -= 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "Hello World"
        o = 5
        self.assertEqual(s.lengthOfLastWord(i), o)

    def test_two(self):
        s = Solution()
        i = "   fly me   to   the moon  "
        o = 4
        self.assertEqual(s.lengthOfLastWord(i), o)

    def test_three(self):
        s = Solution()
        i = "luffy is still joyboy"
        o = 6
        self.assertEqual(s.lengthOfLastWord(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)