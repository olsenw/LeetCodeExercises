# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a sentence text (A sentence is a string of space-separated words) in
    the following format:
    * First letter is in upper case.
    * Each word is text are separated by a single space.

    Rearrange the words in text such that all words are rearranged in an
    increasing order of their lengths. If two words have the same length,
    arrange them in their original order.

    Return the new text following the format above.
    '''
    def arrangeWords(self, text: str) -> str:
        words = text.split()
        order = sorted((len(words[i]), i) for i in range(len(words)))
        answer = words[order[0][1]][0].upper() + words[order[0][1]][1:]
        for (_,i) in order[1:]:
            answer += ' ' + words[i].lower()
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "Leetcode is cool"
        o = "Is cool leetcode"
        self.assertEqual(s.arrangeWords(i), o)

    def test_two(self):
        s = Solution()
        i = "Keep calm and code on"
        o = "On and keep calm code"
        self.assertEqual(s.arrangeWords(i), o)

    def test_three(self):
        s = Solution()
        i = "To be or not to be"
        o = "To be or to be not"
        self.assertEqual(s.arrangeWords(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)