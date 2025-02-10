# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s.

    Remove all digits by doing this operation repeatedly:
    * Delete the first digit and the closet non-digit to its left.

    Return the resulting string after removing all digits.
    '''
    def clearDigits(self, s: str) -> str:
        stack = []
        for c in s:
            if c.isdigit():
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        return "".join(stack)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "abc"
        o = "abc"
        self.assertEqual(s.clearDigits(i), o)

    def test_two(self):
        s = Solution()
        i = "cb34"
        o = ""
        self.assertEqual(s.clearDigits(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)