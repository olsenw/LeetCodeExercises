# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s which consists of lowercase or uppercase letters, return
    the length of the longest palindrome that can be built with those letters.

    Letters are case sensitive, for example, "Aa" is not considered a
    palindrome.
    '''
    def longestPalindrome(self, s: str) -> int:
        answer = 0
        d = set()
        for c in s:
            if c in d:
                answer += 2
                d.remove(c)
            else:
                d.add(c)
        if len(d) > 0:
            answer += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "abccccdd"
        o = 7
        self.assertEqual(s.longestPalindrome(i), o)

    def test_two(self):
        s = Solution()
        i = "a"
        o = 1
        self.assertEqual(s.longestPalindrome(i), o)

    def test_three(self):
        s = Solution()
        i = "Aa"
        o = 1
        self.assertEqual(s.longestPalindrome(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)