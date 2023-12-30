# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of strings words (0-indexed).

    In one operation, pick two distinct indices i and j, where words[i] is a
    non-empty string, and move any character from words[i] to any position in
    words[j].

    Return true if every string in words equal using any number of operations,
    and false otherwise.
    '''
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        c = Counter()
        for word in words:
            for w in word:
                c[w] += 1
        for i in c:
            if c[i] % n:
                return False
        return True

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["abc","aabc","bc"]
        o = True
        self.assertEqual(s.makeEqual(i), o)

    def test_two(self):
        s = Solution()
        i = ["ab","a"]
        o = False
        self.assertEqual(s.makeEqual(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)