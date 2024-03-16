# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of strings of the same length words.

    In one move, it is possible to swap any two even indexed characters or any
    two odd indexed characters of a string words[i].

    Two strings words[i] and words[j] are special-equivalent if after any number
    of moves, words[i] == words[j].

    A group of special-equivalent strings from words is a non-empty subset of
    words such that:
    * Every pair of strings in the group are special equivalent
    * The group is the largest size possible (ie there is not a string words[i]
      not in the group such that words[i] is special-equivalent to every string
      in the group).
    
    Return the number of groups of special-equivalent strings from words.
    '''
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        n = len(words[0])
        h = set()
        for w in words:
            c = [0] * 52
            for i in range(0,n,2):
                c[ord(w[i]) - ord('a')] += 1
            for i in range(1,n,2):
                c[ord(w[i]) - ord('a') + 26] += 1
            h.add(tuple(c))
        return len(h)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["abcd","cdab","cbad","xyzz","zzxy","zzyx"]
        o = 3
        self.assertEqual(s.numSpecialEquivGroups(i), o)

    def test_two(self):
        s = Solution()
        i = ["abc","acb","bac","bca","cab","cba"]
        o = 3
        self.assertEqual(s.numSpecialEquivGroups(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)