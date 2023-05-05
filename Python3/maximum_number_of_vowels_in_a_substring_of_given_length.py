# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s and an integer k, return the maximum number of vowel
    letters in any substring of s with length k.

    Vowel letters in English are 'a', 'e', 'i', 'o', 'u'.
    '''
    def maxVowels(self, s: str, k: int) -> int:
        curr = 0
        for c in s[:k]:
            if c in "aeiou":
                curr += 1
        answer = curr
        for i in range(k, len(s)):
            if s[i - k] in "aeiou":
                curr -= 1
            if s[i] in "aeiou":
                curr += 1
            answer = max(answer, curr)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "abciiidef"
        j = 3
        o = 3
        self.assertEqual(s.maxVowels(i,j), o)

    def test_two(self):
        s = Solution()
        i = "aeiou"
        j = 2
        o = 2
        self.assertEqual(s.maxVowels(i,j), o)

    def test_three(self):
        s = Solution()
        i = "leetcode"
        j = 3
        o = 2
        self.assertEqual(s.maxVowels(i,j), o)

    def test_four(self):
        s = Solution()
        i = "givenastringsandanintegerkreturnthemaximumnumberofvowellettersinanysubstringofswithlengthk"
        j = 4
        o = 2
        self.assertEqual(s.maxVowels(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)