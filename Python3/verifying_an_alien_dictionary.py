# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from itertools import zip_longest
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    In an alien language, surprisingly, they also use English lowercase letters,
    but possibly in a different order. The order of the alphabet is some
    permutation of lowercase letters.

    Given a sequence of words written in the alien language, and the order of
    the alphabet, return true if and only if the given words sorted
    lexicographically in this alien language.
    '''
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) == 1:
            return True
        mapping = {order[i]:i for i in range(26)}
        mapping[None] = -1
        def isLex(a,b):
            for i,j in zip_longest(a,b):
                if i != j:
                    break
            return mapping[i] <= mapping[j]
        return all(isLex(words[i - 1], words[i]) for i in range(1, len(words)))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["hello","leetcode"]
        j = "hlabcdefgijkmnopqrstuvwxyz"
        o = True
        self.assertEqual(s.isAlienSorted(i,j), o)

    def test_two(self):
        s = Solution()
        i = ["word","world","row"]
        j = "worldabcefghijkmnpqstuvxyz"
        o = False
        self.assertEqual(s.isAlienSorted(i,j), o)

    def test_three(self):
        s = Solution()
        i = ["apple","app"]
        j = "abcdefghijklmnopqrstuvwxyz"
        o = False
        self.assertEqual(s.isAlienSorted(i,j), o)

    def test_four(self):
        s = Solution()
        i = ["hello","hello"]
        j = "abcdefghijklmnopqrstuvwxyz"
        o = True
        self.assertEqual(s.isAlienSorted(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)