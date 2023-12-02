# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of strings words and a string chars.

    A string is good if it can be formed by characters from chars (each
    character can only be used once).

    Return the sum of lengths of all good strings in words.
    '''
    def countCharacters(self, words: List[str], chars: str) -> int:
        def f(a):
            c = [0] * 26
            for b in a:
                c[ord(b) - ord('a')] += 1
            return c
        target = f(chars)
        counts = [f(w) for w in words]
        return sum(len(words[i]) for i in range(len(words)) if all(j <= k for j,k in zip(counts[i], target)))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["cat","bt","hat","tree"]
        j = "atach"
        o = 6
        self.assertEqual(s.countCharacters(i,j), o)

    def test_two(self):
        s = Solution()
        i = ["hello","world","leetcode"]
        j = "welldonehoneyr"
        o = 10
        self.assertEqual(s.countCharacters(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)