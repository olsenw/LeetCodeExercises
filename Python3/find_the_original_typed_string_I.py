# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Alice is attempting to type a specific string on here computer. However, she
    tends to be clumsy and may press a key for too long, resulting in a
    character being typed multiple times.

    Although Alich tried to focus on her typing, she is aware that she may still
    have done this at most once.

    Given is a string word, which represents the final output displayed on
    Alice's screen.

    Return the total number of possible original strings that Alice might have
    intended to type.
    '''
    # fails (double counts final cases where all characters used)
    def possibleStringCount_double_count(self, word: str) -> int:
        answer = 1
        count = 1
        last = ""
        for w in word:
            if w != last:
                last = w
                answer *= count
                count = 1
            else:
                count += 1
        return answer * count

    # brute force save all combinations
    def possibleStringCount_brute(self, word: str) -> int:
        word += "$"
        possible = set()
        i = 0
        last = word[0]
        for j,w in enumerate(word):
            if w != last:
                for k in range(1, j - i + 1):
                    possible.add(word[:i] + last * k + word[j:])
                i = j
                last = w
        return len(possible)

    # based on LeetCode editorial
    # https://leetcode.com/problems/find-the-original-typed-string-i/editorial/?envType=daily-question&envId=2025-07-01
    def possibleStringCount(self, word: str) -> int:
        answer = 1
        for i in range(1, len(word)):
            if word[i-1] == word[i]:
                answer += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "abbcccc"
        o = 5
        self.assertEqual(s.possibleStringCount(i), o)

    def test_two(self):
        s = Solution()
        i = "abcd"
        o = 1
        self.assertEqual(s.possibleStringCount(i), o)

    def test_three(self):
        s = Solution()
        i = "aaaa"
        o = 4
        self.assertEqual(s.possibleStringCount(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)