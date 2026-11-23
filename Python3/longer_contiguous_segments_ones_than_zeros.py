# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a binary string s, return true if the longest contiguous segment of
    1's is strictly longer than the longest contiguous segment of 0's in s, or
    return false otherwise.

    Note that if there are no 0's, then the longest continuous segment of 0's is
    considered to have a length 0. The same applies if there is no 1's.
    '''
    def checkZeroOnes(self, s: str) -> bool:
        s += '3'
        ones = 0
        zeros = 0
        last = s[0]
        current = 1
        for i in range(1,len(s)):
            if s[i] == last:
                current += 1
            else:
                if last == '1':
                    ones = max(ones,current)
                else:
                    zeros = max(zeros, current)
                current = 1
                last = s[i]
        return ones > zeros

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "1101"
        o = True
        self.assertEqual(s.checkZeroOnes(i), o)

    def test_two(self):
        s = Solution()
        i = "111000"
        o = False
        self.assertEqual(s.checkZeroOnes(i), o)

    def test_three(self):
        s = Solution()
        i = "110100010"
        o = False
        self.assertEqual(s.checkZeroOnes(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)