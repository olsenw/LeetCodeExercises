# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    A substring is a contiguous (non-empty) sequence of characters within a
    string.

    A vowel substring is a substring that only consists of vowels ('a','e','i',
    'o', and 'u') and has all five vowels present in it.

    Given a string word, return the number of vowel substrings in word.
    '''
    # brute force
    def countVowelSubstrings(self, word: str) -> int:
        n = len(word)
        answer = 0
        for i in range(n):
            c = Counter()
            if word[i] in "aeiou":
                for j in range(i, n):
                    if word[j] not in "aeiou":
                        break
                    c[word[j]] += 1
                    if all(c[k] > 0 for k in "aeiou"):
                        answer += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "aeiouu"
        o = 2
        self.assertEqual(s.countVowelSubstrings(i), o)

    def test_two(self):
        s = Solution()
        i = "unicornarihan"
        o = 0
        self.assertEqual(s.countVowelSubstrings(i), o)

    def test_three(self):
        s = Solution()
        i = "cuaieuouac"
        o = 7
        self.assertEqual(s.countVowelSubstrings(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)