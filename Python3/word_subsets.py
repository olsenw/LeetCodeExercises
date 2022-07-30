# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

from collections import Counter

class Solution:
    '''
    Given two string arrays words1 and words2.

    A string b is a subset of string a if every letter in b occurs in a
    including multiplicity.

    A string a from words1 is universal if for every string b in words2,
    b is a subset of a.

    Return an array of all the universal strings in words1. The answer
    may be in any order.
    '''
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        answer = []
        universal = Counter()
        for w in words2:
            c = Counter(w)
            for i in c:
                if i in universal:
                    universal[i] = max(universal[i], c[i])
                else:
                    universal[i] = c[i]
        for w in words1:
            c = Counter(w)
            for i in universal:
                if i not in c or c[i] < universal[i]:
                    break
            else:
                answer.append(w)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["amazon","apple","facebook","google","leetcode"]
        j = ["e","o"]
        o = ["facebook","google","leetcode"]
        self.assertEqual(s.wordSubsets(i,j), o)

    def test_two(self):
        s = Solution()
        i = ["amazon","apple","facebook","google","leetcode"]
        j = ["l","e"]
        o = ["apple","google","leetcode"]
        self.assertEqual(s.wordSubsets(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)