# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    Given a string s, return the maximum length of a substring such that it
    contains at most two occurrences of each character.
    '''
    def maximumLengthSubstring(self, s: str) -> int:
        answer = 0
        c = Counter()
        i = 0
        for j in range(len(s)):
            c[s[j]] += 1
            while i < j and c[s[j]] > 2:
                c[s[i]] -= 1
                i += 1
            answer = max(answer, j - i + 1)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "bcbbbcba"
        o = 4
        self.assertEqual(s.maximumLengthSubstring(i), o)

    def test_two(self):
        s = Solution()
        i = "aaaa"
        o = 2
        self.assertEqual(s.maximumLengthSubstring(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)