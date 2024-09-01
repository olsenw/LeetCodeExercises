# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s consisting of lowercase English letters, return the first
    letter to appear twice.

    Note:
    * A letter a appears twice before another letter b if the second occurrence
      of a is before the second occurrence of b.
    * s will contain at least one letter that appears twice.
    '''
    def repeatedCharacter(self, s: str) -> str:
        a = set()
        for c in s:
            if c in a:
                return c
            else:
                a.add(c)
        return None

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "abccbaacz"
        o = "c"
        self.assertEqual(s.repeatedCharacter(i), o)

    def test_two(self):
        s = Solution()
        i = "abcdd"
        o = "d"
        self.assertEqual(s.repeatedCharacter(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)