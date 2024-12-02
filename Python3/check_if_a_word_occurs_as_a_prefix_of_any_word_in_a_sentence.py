# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a sentence that consists of some words separated by a single space,
    and a searchWord, check if searchWord is a prefix of any word in sentence.

    Return the index of the word in sentence (1-indexed) where searchWord is a
    prefix of this word. If searchWord is a prefix of more than one word, return
    the index of the first word (minimum index). If there is no such word return
    -1.

    A prefix of a string s is any leading contiguous substring of s.
    '''
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i,j in enumerate(sentence.split()):
            if j.startswith(searchWord):
                return i + 1
        return -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "i love eating burger"
        j = "burg"
        o = 4
        self.assertEqual(s.isPrefixOfWord(i,j), o)

    def test_two(self):
        s = Solution()
        i = "this problem is an easy problem"
        j = "pro"
        o = 2
        self.assertEqual(s.isPrefixOfWord(i,j), o)

    def test_three(self):
        s = Solution()
        i = "i am tired"
        j = "you"
        o = -1
        self.assertEqual(s.isPrefixOfWord(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)