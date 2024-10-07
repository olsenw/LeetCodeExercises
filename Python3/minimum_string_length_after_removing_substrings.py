# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s consisting only of uppercase English letters.

    An operation can be applied many times to this string. In one operation it
    is possible to remove any occurrence of one of the substrings "AB" or "CD"
    from s.

    Return the minimum possible length of the resulting string that can be
    obtained after applying the above operation.

    Note that the string concatenates after removing the substring and could
    produce new "AB" or "CD" substrings.
    '''
    def minLength(self, s: str) -> int:
        stack = []
        for c in s:
            stack.append(c)
            while len(stack) > 1 and ((stack[-2] == 'A' and stack[-1] == 'B') or (stack[-2] == 'C' and stack[-1] == 'D')):
                stack.pop()
                stack.pop()
        return len(stack)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "ABFCACDB"
        o = 2
        self.assertEqual(s.minLength(i), o)

    def test_two(self):
        s = Solution()
        i = "ACBBD"
        o = 5
        self.assertEqual(s.minLength(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)