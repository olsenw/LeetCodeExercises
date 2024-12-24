# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string num consisting of only digits. A string of digits is called
    balanced if the sum of the digits at even indices is equal to the sum of
    digits at odd indices.

    Return true if num is balanced, otherwise return false.
    '''
    def isBalanced(self, num: str) -> bool:
        num = [int(n) for n in num]
        return sum(num[::2]) == sum(num[1::2])

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "1234"
        o = False
        self.assertEqual(s.isBalanced(i), o)

    def test_two(self):
        s = Solution()
        i = "24123"
        o = True
        self.assertEqual(s.isBalanced(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)