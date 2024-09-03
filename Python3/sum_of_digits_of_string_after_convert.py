# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s consisting of lowercase English letters, and an integer k.

    First, convert s into an integer by replacing each letter with its position
    in the alphabet (ie replace 'a' with 1, 'b' with 2, ..., 'z' with 26). Then,
    transform the integer by replacing it with the sum of its digits. Repeat the
    transform operation k times in total.

    Return the resulting integer after performing the operations described
    above.
    '''
    def getLucky(self, s: str, k: int) -> int:
        s = "".join(str(ord(c)-96) for c in s)
        for _ in range(k):
            s = str(sum(int(c) for c in s))
        return int(s)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "iiii", 1
        o = 36
        self.assertEqual(s.getLucky(*i), o)

    def test_two(self):
        s = Solution()
        i = "leetcode", 2
        o = 6
        self.assertEqual(s.getLucky(*i), o)

    def test_three(self):
        s = Solution()
        i = "zbax", 2
        o = 8
        self.assertEqual(s.getLucky(*i), o)

    def test_three(self):
        s = Solution()
        i = "z" * 100, 1
        o = 8
        self.assertEqual(s.getLucky(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)