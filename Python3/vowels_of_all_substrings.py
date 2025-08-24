# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string word, return the sum of the number of vowels
    ('a', 'e', 'i', 'o', and 'u') in every substring of word.

    A substring is a contiguous (non-empty) sequence of character within a
    string.
    '''
    # def countVowels_brute(self, word: str) -> int:
    def countVowels(self, word: str) -> int:
        n = len(word)
        counts = [0] * n
        for width in range(1,n+1):
            for i in range(n - width + 1):
                for j in range(i, i + width):
                    counts[j] += 1
        return sum(counts[i] for i in range(n) if word[i] in "aeiou")

    # based on editorial by Abhishek Jha
    # https://leetcode.com/problems/vowels-of-all-substrings/solutions/1564075/detailed-explanation-of-why-len-pos-pos-1-works/?envType=problem-list-v2&envId=ng5yboc7
    # a character can be in any substring such that i <= pos <= j
    # where 0 <= i <= pos and pos <= j <= len(word)
    # for a given position there are (len - pos) * (pos + 1) substrings
    def countVowels(self, word: str) -> int:
        n = len(word)
        answer = 0
        for pos,c in enumerate(word):
            if c not in "aeiou":
                continue
            answer += (n - pos) * (pos + 1)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "aba"
        o = 6
        self.assertEqual(s.countVowels(i), o)

    def test_two(self):
        s = Solution()
        i = "abc"
        o = 3
        self.assertEqual(s.countVowels(i), o)

    def test_three(self):
        s = Solution()
        i = "ltcd"
        o = 0
        self.assertEqual(s.countVowels(i), o)

    def test_four(self):
        s = Solution()
        i = "aaaaaaaa"
        o = 120
        self.assertEqual(s.countVowels(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)