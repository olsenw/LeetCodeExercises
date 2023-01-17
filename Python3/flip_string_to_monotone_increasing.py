# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    A binary string is monotone increasing if it consists of some number of 0's
    (possibly node), followed by some number of 1's (also possibly none).

    Given a binary string s. Is is possible to flip s[i], changing it from 0 to 
    1 or from 1 to 0.

    Return the minimum number of flips to make s monotone increasing.
    '''
    def minFlipsMonoIncr(self, s: str) -> int:
        one = [0 if s[-1] == '1' else 1] * len(s)
        for i in range(len(s) - 2, -1, -1):
            one[i] = one[i + 1] + (1 if s[i] == '0' else 0)
        zero = [0 if s[0] == '0' else 1] * len(s)
        for i in range(1, len(s)):
            zero[i] = zero[i - 1] + (1 if s[i] == '1' else 0)
        a = [0] * len(s)
        a[0] = one[0]
        for i in range(1,len(s)-1):
            a[i] = zero[i-1] + one[i+1]
        a[-1] = zero[-1]
        return min(a)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "00110"
        o = 1
        self.assertEqual(s.minFlipsMonoIncr(i), o)

    def test_two(self):
        s = Solution()
        i = "010110"
        o = 2
        self.assertEqual(s.minFlipsMonoIncr(i), o)

    def test_three(self):
        s = Solution()
        i = "00011000"
        o = 2
        self.assertEqual(s.minFlipsMonoIncr(i), o)

    def test_four(self):
        s = Solution()
        i = "0101100011"
        o = 3
        self.assertEqual(s.minFlipsMonoIncr(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)