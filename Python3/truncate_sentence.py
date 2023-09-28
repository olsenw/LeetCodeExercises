# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A sentence is a list of words that are separated by a single space with no
    leading or trailing spaces. Each of the words consists of only uppercase and
    lowercase English letters (no punctuation).

    Given a sentence s and an integer k. Truncate s such that it contains only
    the first k words. Return s after truncating it.
    '''
    def truncateSentence(self, s: str, k: int) -> str:
        a = ""
        for c in s:
            if c == " ":
                k -= 1
            if k == 0:
                break
            a += c
        return a

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "Hello how are you Contestant"
        j = 4
        o = "Hello how are you"
        self.assertEqual(s.truncateSentence(i,j), o)

    def test_two(self):
        s = Solution()
        i = "What is the solution to this problem"
        j = 4
        o = "What is the solution"
        self.assertEqual(s.truncateSentence(i,j), o)

    def test_three(self):
        s = Solution()
        i = "chopper is not a tanuki"
        j = 5
        o = "chopper is not a tanuki"
        self.assertEqual(s.truncateSentence(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)