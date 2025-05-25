# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string licensePlate and an array of strings words, find the shortest
    completing words in words.

    A completing word is a word that contains all the letters in licensePlate.
    Ignore numbers and spaces in licensePlate, and treat letters as case
    insensitive. If a letter appears more than once in licensePlate, then it
    must appear in the word the same number of times or more.

    Return the shortest completing word in words, it is guaranteed an answer
    exists. If there are multiple shortest completing words, return the first
    one that occurs in words.
    '''
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        c = Counter(i for i in licensePlate.lower() if i.isalpha())
        words.sort(key=lambda x: len(x))
        for w in words:
            t = Counter(w)
            if all(c[i] <= t[i] for i in c):
                return w
        return "123456"

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "1s3 PSt"
        j = ["step","steps","stripe","stepple"]
        o = "steps"
        self.assertEqual(s.shortestCompletingWord(i,j), o)

    def test_two(self):
        s = Solution()
        i = "1s3 456"
        j = ["looks","pest","stew","show"]
        o = "pest"
        self.assertEqual(s.shortestCompletingWord(i,j), o)

    def test_three(self):
        s = Solution()
        i = "B687015"
        j = ["born","give","would","nice","in","understand","blue","force","have","that"]
        o = "born"
        self.assertEqual(s.shortestCompletingWord(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)