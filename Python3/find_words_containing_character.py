# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed array of string words and a character x.

    Return an array of indices representing the words that contain the character
    x.

    Note that the returned array may be in any order.
    '''
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i,j in enumerate(words) if x in j]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["leet","code"]
        j = "e"
        o = [0,1]
        self.assertEqual(s.findWordsContaining(i,j), o)

    def test_two(self):
        s = Solution()
        i = ["abc","bcd","aaaa","cbc"]
        j = "a"
        o = [0,2]
        self.assertEqual(s.findWordsContaining(i,j), o)

    def test_three(self):
        s = Solution()
        i = ["abc","bcd","aaaa","cbc"]
        j = "z"
        o = []
        self.assertEqual(s.findWordsContaining(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)