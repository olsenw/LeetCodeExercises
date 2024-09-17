# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    A sentence is a string of single-space separated words where each word
    consists only of lowercase letters.

    A word is uncommon if it appears exactly once in one of the sentences, and
    does not appear in the other sentence.

    Given two sentences s1 and s2, return a list of all the uncommon words. The
    answer may be returned in any order.
    '''
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = Counter(s1.split())
        s2 = Counter(s2.split())
        answer = []
        for w in s1:
            if s1[w] == 1 and w not in s2:
                answer.append(w)
        for w in s2:
            if s2[w] == 1 and w not in s1:
                answer.append(w)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "this apple is sweet", "this apple is sour"
        o = ["sweet","sour"]
        self.assertEqual(s.uncommonFromSentences(*i), o)

    def test_two(self):
        s = Solution()
        i = "apple apple", "banana"
        o = ["banana"]
        self.assertEqual(s.uncommonFromSentences(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)