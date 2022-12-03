# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a string s, sort it in decreasing order based on the frequency of the
    characters. The frequency of a character is the number of times it appears
    in the string.

    Return the sorted string. If there are multiple answers, return any of them.
    '''
    def frequencySort_Counter(self, s: str) -> str:
        c = Counter(s)
        a = ""
        for i,j in c.most_common():
            a += i * j
        return a

    def frequencySort(self, s: str) -> str:
        d = {}
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        return ''.join(i * j for i,j in sorted([(d[c],c) for c in d], reverse=True))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "tree"
        o = "eert"
        self.assertEqual(s.frequencySort(i), o)

    def test_two(self):
        s = Solution()
        i = "cccaaa"
        o = "aaaccc"
        self.assertEqual(s.frequencySort(i), o)

    def test_three(self):
        s = Solution()
        i = "Aabb"
        o = "bbAa"
        self.assertEqual(s.frequencySort(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)