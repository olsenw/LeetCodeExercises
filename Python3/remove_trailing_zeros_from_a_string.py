# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a positive integer nums represented as a string, return the integer
    num without trailing zeros as a string.
    '''
    def removeTrailingZeros_slow(self, num: str) -> str:
        for i in range(len(num)-1,-1,-1):
            if num[i] != '0':
                break
        return num[:i+1]

    def removeTrailingZeros(self, num: str) -> str:
        return num.rstrip('0')

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "51230100"
        o = "512301"
        self.assertEqual(s.removeTrailingZeros(i), o)

    '''
    this is an invalid test case given the problem parameters
    '''
    # def test_two(self):
    #     s = Solution()
    #     i = "0000"
    #     o = "0"
    #     self.assertEqual(s.removeTrailingZeros(i), o)

    def test_three(self):
        s = Solution()
        i = "123"
        o = "123"
        self.assertEqual(s.removeTrailingZeros(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)