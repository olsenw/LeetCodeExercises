# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer n.

    Return the total number of commas used when writing all integers from [1,n]
    (inclusive) in standard number formatting.

    In standard formatting:
    * A comma is inserted after every three digits from the right.
    * Numbers with fewer than 4 digits contain no commas.
    '''
    def countCommas(self, n: int) -> int:
        # answer, n = divmod(n, 1000)
        return max(n - 999, 0)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 1002
        o = 3
        self.assertEqual(s.countCommas(i), o)

    def test_two(self):
        s = Solution()
        i = 998
        o = 0
        self.assertEqual(s.countCommas(i), o)

    def test_three(self):
        s = Solution()
        i = 10000
        o = 9001
        self.assertEqual(s.countCommas(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)