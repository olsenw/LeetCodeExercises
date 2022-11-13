# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an input string s, reverse the order of the words.
    
    A word is defined as a sequence of non-space characters. The words in s will
    be separated by at least one space.
    
    Return a string of the words in reverse order concatenated by a single
    space.
    
    Note that s may contain leading or trailing spaces or multiple spaces
    between two words. The returned string should only have a single space
    separating the words. Do not include any extra spaces.
    '''
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "the sky is blue"
        o = "blue is sky the"
        self.assertEqual(s.reverseWords(i), o)

    def test_two(self):
        s = Solution()
        i = "  hello world  "
        o = "world hello"
        self.assertEqual(s.reverseWords(i), o)

    def test_three(self):
        s = Solution()
        i = "a good   example"
        o = "example good a"
        self.assertEqual(s.reverseWords(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)