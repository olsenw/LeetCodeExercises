# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There is a special typewriter with lowercase English letters 'a' to 'z'
    arranged in a circle with a pointer. A character can only be typed if the
    pointer is pointing to that character. The pointer is initially pointing to
    the character 'a'.

    Each second, one of the following operations may be performed:
    * Move the pointer one character counterclockwise or clockwise.
    * Type the character the pointer is currently on.

    Given a string word, return the minimum number of seconds to type out the
    characters in word.
    '''
    # does not go backwards correctly
    def minTimeToType_wrong(self, word: str) -> int:
        answer = len(word)
        curr = 'a'
        for i in range(len(word)):
            if word[i] > curr:
                answer += ord(word[i]) - ord(curr)
            else:
                answer += ord(curr) - ord(word[i])
            curr = word[i]
        return answer
    
    # way overthinking how to do the left/right move
    # looked at solution (unsure which) on how to do the math
    def minTimeToType(self, word: str) -> int:
        n = len(word)
        answer = len(word)
        curr = 0
        for c in word:
            c = ord(c) - 97
            if curr < c:
                answer += min(c - curr, 26 + curr - c)
            else:
                answer += min(curr - c, 26 + c - curr)
            curr = c
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "abc"
        o = 5
        self.assertEqual(s.minTimeToType(i), o)

    def test_two(self):
        s = Solution()
        i = "bza"
        o = 7
        self.assertEqual(s.minTimeToType(i), o)

    def test_three(self):
        s = Solution()
        i = "zjpc"
        o = 34
        self.assertEqual(s.minTimeToType(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)