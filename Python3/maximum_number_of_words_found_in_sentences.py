# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A sentence is a list of words that are separated by a single space with no
    leading or trailing spaces.

    Given an array of strings sentences, where each sentences[i] represents a
    single sentence.

    Return the maximum number of words that appear in a single sentence.
    '''
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(len(s.split()) for s in sentences)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
        o = 6
        self.assertEqual(s.mostWordsFound(i), o)

    def test_two(self):
        s = Solution()
        i = ["please wait", "continue to fight", "continue to win"]
        o = 3
        self.assertEqual(s.mostWordsFound(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)