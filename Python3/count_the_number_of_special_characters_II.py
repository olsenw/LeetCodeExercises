# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string word. A letter c is called special if it appears both in
    lowercase and uppercase in word, and every lowercase occurrence of c appears
    before the first uppercase occurrence of c.

    Return the number of special letters in word.
    '''
    def numberOfSpecialChars(self, word: str) -> int:
        lower = dict()
        upper = dict()
        for i,j in enumerate(word):
            if j.islower():
                lower[j] = i
            elif j not in upper:
                upper[j] = i
        answer = 0
        for i,j in zip("abcdefghijklmnopqrstuvwxyz","ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            if i not in lower:
                continue
            if j not in upper:
                continue
            if lower[i] < upper[j]:
                answer += 1
        return answer

    # based on faster submitted solutions
    def numberOfSpecialChars(self, word: str) -> int:
        answer = 0
        for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            upper = word.find(c)
            if upper >= 0:
                c = c.lower()
                lower = word.rfind(c)
                if lower >= 0 and lower < upper:
                    answer += 1
        return answer

    def numberOfSpecialChars(self, word: str) -> int:
        n = len(word)
        upper = [n] * 26
        lower = [n] * 26
        for i,j in enumerate(word):
            if j.islower():
                lower[ord(j) - 97] = i
            else:
                upper[ord(j) - 65] = min(upper[ord(j) - 65], i)
        pass
        return sum(upper[i] < n and lower[i] < upper[i] for i in range(26))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "aaAbcBC"
        o = 3
        self.assertEqual(s.numberOfSpecialChars(i), o)

    def test_two(self):
        s = Solution()
        i = "abc"
        o = 0
        self.assertEqual(s.numberOfSpecialChars(i), o)

    def test_three(self):
        s = Solution()
        i = "AbBCab"
        o = 0
        self.assertEqual(s.numberOfSpecialChars(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)