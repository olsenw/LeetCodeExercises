# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s, return the maximum number of unique substrings that the
    given string can be split into.

    It is possible to split string s into any list of non-empty substrings,
    where the concatenation of the substrings forms the original string.
    However, each substring must be unique.

    A substring is contiguous sequence of characters within a string.
    '''
    # hints are helpful
    # that and realizing that it can be split using a binary tree
    def maxUniqueSplit(self, s: str) -> int:
        answer = 1
        seen = set()
        def split(s):
            if s == "":
                nonlocal answer
                answer = max(answer, len(seen))
                return
            c = ""
            for i in range(len(s)):
                c += s[i]
                if len(c) > 0 and c not in seen:
                    seen.add(c)
                    split(s[i+1:])
                    seen.remove(c)
        split(s)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "ababccc"
        o = 5
        self.assertEqual(s.maxUniqueSplit(i), o)

    def test_two(self):
        s = Solution()
        i = "aba"
        o = 2
        self.assertEqual(s.maxUniqueSplit(i), o)

    def test_three(self):
        s = Solution()
        i = "aa"
        o = 1
        self.assertEqual(s.maxUniqueSplit(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)