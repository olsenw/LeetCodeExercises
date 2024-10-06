# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two strings sentence1 and sentence2, each representing a sentence
    composed of words. A sentence is a list of words that are separated by a
    single space with no leading or trailing spaces. Each word consists of only
    uppercase and lowercase English characters.

    Two sentences s1 and s2 are considered similar if it is possible to insert
    an arbitrary sentence (possibly empty) inside of these sentences such that
    the two sentences become equal. Note that inserted sentence must be
    separated from existing words by spaces.

    Given two sentences sentence1 and sentence2, return true if sentence1 and
    sentence2 are similar. Otherwise, return false.
    '''
    # only works for matching beginning or ending of string
    def areSentencesSimilar_fails(self, sentence1: str, sentence2: str) -> bool:
        s1 = sentence1.split()
        s2 = sentence2.split()
        if s1[0] == s2[0]:
            for i,j in zip(s1, s2):
                if i != j:
                    return False
            return True
        elif s1[-1] == s2[-1]:
            for i,j in zip(s1[::-1], s2[::-1]):
                if i != j:
                    return False
            return True
        return False

    # slow
    def areSentencesSimilar_passes(self, sentence1: str, sentence2: str) -> bool:
        s1 = deque(sentence1.split())
        s2 = deque(sentence2.split())
        if len(s1) < len(s2):
            s1, s2 = s2, s1
        while s2 and s1[0] == s2[0]:
            s1.popleft()
            s2.popleft()
        while s2 and s1[-1] == s2[-1]:
            s1.pop()
            s2.pop()
        return len(s2) == 0

    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = list(sentence1.split())
        s2 = list(sentence2.split())
        if len(s1) < len(s2):
            s1, s2 = s2, s1
        i,j = 0, len(s1) - 1
        a,b = 0, len(s2) - 1
        while a <= b and s1[i] == s2[a]:
            i += 1
            a += 1
        while a <= b and s1[j] == s2[b]:
            j -= 1
            b -= 1
        return b < a

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "My name is Haley"
        j = "My Haley"
        o = True
        self.assertEqual(s.areSentencesSimilar(i,j), o)

    def test_two(self):
        s = Solution()
        i = "of"
        j = "A lot of words"
        o = False
        self.assertEqual(s.areSentencesSimilar(i,j), o)

    def test_three(self):
        s = Solution()
        i = "Eating right now"
        j = "Eating"
        o = True
        self.assertEqual(s.areSentencesSimilar(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)