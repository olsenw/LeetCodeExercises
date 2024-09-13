# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string allowed consisting of distinct characters and an array of
    strings words. A string is consistent if all characters in the string appear
    in the string allowed.

    Return the number of consistent strings in the array words.
    '''
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        answer = 0
        allowed = set(allowed)
        for w in words:
            if set(w).issubset(allowed):
                answer += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "ab", ["ad","bd","aaab","baa","badab"]
        o = 2
        self.assertEqual(s.countConsistentStrings(*i), o)

    def test_two(self):
        s = Solution()
        i = "abc", ["a","b","c","ab","ac","bc","abc"]
        o = 7
        self.assertEqual(s.countConsistentStrings(*i), o)

    def test_three(self):
        s = Solution()
        i = "cad", ["cc","acd","b","ba","bac","bad","ac","d"]
        o = 4
        self.assertEqual(s.countConsistentStrings(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)