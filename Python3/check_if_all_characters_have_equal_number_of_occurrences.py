# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s, return true if s is a good string, or false otherwise.

    A string s is good if all the characters that appear in s have the same
    number of occurrences (ie, the same frequency).
    '''
    def areOccurrencesEqual(self, s: str) -> bool:
        c = Counter(s)
        a = c[s[0]]
        for i in c:
            if c[i] != a:
                return False
        return True

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "abacbc"
        o = True
        self.assertEqual(s.areOccurrencesEqual(i), o)

    def test_two(self):
        s = Solution()
        i = "aaabb"
        o = False
        self.assertEqual(s.areOccurrencesEqual(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)