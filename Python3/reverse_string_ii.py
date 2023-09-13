# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s and an integer k, reverse the first k characters for every
    2k characters counting from the start of the string.
    
    If there are fewer than k characters left, reverse all of them. If there are
    less than 2k but greater than or equal to k characters, then reverse the
    first k characters and leave the other as original.
    '''
    def reverseStr(self, s: str, k: int) -> str:
        answer = ""
        a,b = "", ""
        for c in s:
            if len(b) == k:
                answer += a[::-1] + b
                a = ""
                b = ""
            if len(a) < k:
                a += c
            else:
                b += c
        return answer + a[::-1] + b

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "abcdefg"
        j = 2
        o = "bacdfeg"
        self.assertEqual(s.reverseStr(i,j), o)

    def test_two(self):
        s = Solution()
        i = "abcd"
        j = 2
        o = "bacd"
        self.assertEqual(s.reverseStr(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)