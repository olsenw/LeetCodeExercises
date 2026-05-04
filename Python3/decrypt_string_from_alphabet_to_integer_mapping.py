# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s formed by digits and '#'. Map s to English lowercase
    English lowercase characters as follows:
    * Characters ('a' to 'i') are represented by ('1' to '9') respectively.
    * Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.

    Return the string formed after mapping.

    The test cases are generated so that a unique mapping will always exist.
    '''
    mapping = {str(i):j for i,j in zip(range(1,27),"abcdefghijklmnopqrstuvwxyz")}
    def freqAlphabets_fails(self, s: str) -> str:
        answer = ""
        for c in s.split('#'):
            for w in c[:-2]:
                answer += self.mapping[w]
            answer += self.mapping[c[-2:]]
        return answer

    def freqAlphabets(self, s: str) -> str:
        stack = []
        i = len(s)-1
        while i >= 0:
            if s[i] == '#':
                stack.append(self.mapping[s[i-2:i]])
                i -= 3
            else:
                stack.append(self.mapping[s[i]])
                i -= 1
        return ''.join(stack[::-1])

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "10#11#12"
        o = "jkab"
        self.assertEqual(s.freqAlphabets(i), o)

    def test_two(self):
        s = Solution()
        i = "1326#"
        o = "acz"
        self.assertEqual(s.freqAlphabets(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)