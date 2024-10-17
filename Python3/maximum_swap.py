# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer num, swap at most two digits to get the maximum value
    number.

    Return the maximum value number that can be obtained.
    '''
    def maximumSwap(self, num: int) -> int:
        s = str(num)
        t = sorted(s,reverse=True)
        i = 0
        while i < len(s):
            if s[i] != t[i]:
                break
            i += 1
        if i == len(s):
            return num
        for j in range(len(s)-1,i,-1):
            if s[j] == t[i]:
                break
        return int(s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:])

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 2736
        o = 7236
        self.assertEqual(s.maximumSwap(i), o)

    def test_two(self):
        s = Solution()
        i = 9973
        o = 9973
        self.assertEqual(s.maximumSwap(i), o)

    def test_three(self):
        s = Solution()
        i = 997993
        o = 999973
        self.assertEqual(s.maximumSwap(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)