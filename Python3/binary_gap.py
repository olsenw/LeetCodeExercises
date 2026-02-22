# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a positive integer n, find and return the longest distance between any
    tow adjacent 1's in the binary representation of n. If there are no two
    adjacent 1's return 0.

    Two 1's are adjacent if there are only 0's separating them (possibly no
    0's). The distance between two 1's is the absolute difference between their
    bit positions.
    '''
    def binaryGap(self, n: int) -> int:
        answer = 0
        n = bin(n)
        last = n.find('1')
        for i in range(last + 1, len(n)):
            if n[i] == '1':
                answer = max(answer, i - last)
                last = i
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 22
        o = 2
        self.assertEqual(s.binaryGap(i), o)

    def test_two(self):
        s = Solution()
        i = 8
        o = 0
        self.assertEqual(s.binaryGap(i), o)

    def test_three(self):
        s = Solution()
        i = 5
        o = 2
        self.assertEqual(s.binaryGap(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)