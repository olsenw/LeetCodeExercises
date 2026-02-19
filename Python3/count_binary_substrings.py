# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a binary string s, return the number of non-empty substrings that have
    the same number of of 0's and 1's and all the 0's and all the 1's in these
    substrings are grouped consecutively.

    Substrings that occur multiple times are counted the number of times they
    occur.
    '''
    def countBinarySubstrings(self, s: str) -> int:
        answer = 0
        zeros = 0
        ones = 0
        # count zero then one substrings
        for c in s:
            if ones > 0 and c == '0':
                answer += min(zeros,ones)
                zeros = 1
                ones = 0
            elif c =='1':
                ones += 1
            else:
                zeros += 1
            pass
        answer += min(zeros,ones)
        zeros = 0
        ones = 0
        # count one then zero substrings
        for c in s:
            if zeros > 0 and c == '1':
                answer += min(zeros,ones)
                zeros = 0
                ones = 1
            elif c =='1':
                ones += 1
            else:
                zeros += 1
            pass
        answer += min(zeros,ones)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "00110011"
        o = 6
        self.assertEqual(s.countBinarySubstrings(i), o)

    def test_two(self):
        s = Solution()
        i = "10101"
        o = 4
        self.assertEqual(s.countBinarySubstrings(i), o)

    def test_three(self):
        s = Solution()
        i = "11110000"
        o = 4
        self.assertEqual(s.countBinarySubstrings(i), o)

    def test_four(self):
        s = Solution()
        i = "00001111"
        o = 4
        self.assertEqual(s.countBinarySubstrings(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)