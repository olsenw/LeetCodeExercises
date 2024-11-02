# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A sentence is a list of words that are separated by a single space with no
    leading or trailing spaces.

    Words consist of only uppercase and lowercase English letters. Uppercase and
    lowercase English letters are considered different.

    A sentence is circular if:
    * The last character of a word is equal to the first character of the next
      word.
    * The last character of the last word is equal to the first character of the
      first word.

    Given a string sentence, return true if it is circular. Otherwise, return
    false.
    '''
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0] != sentence[-1]:
            return False
        for i in range(len(sentence)):
            if sentence[i] == " " and sentence[i-1] != sentence[i+1]:
                return False
        return True

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "leetcode exercises sound delightful"
        o = True
        self.assertEqual(s.isCircularSentence(i), o)

    def test_two(self):
        s = Solution()
        i = "eetcode"
        o = True
        self.assertEqual(s.isCircularSentence(i), o)

    def test_three(self):
        s = Solution()
        i = "Leetcode is cool"
        o = False
        self.assertEqual(s.isCircularSentence(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)