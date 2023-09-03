# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s, reorder the string using the following algorithm:
    
    1. Pick the smallest character from s and append it to the result.
    2. Pick the smallest character from s which is greater than the last
       appended character to the result and append it.
    3. Repeat step 2 until it is impossible to pick more characters.
    4. Pick the largest character from s and append it to the result.
    5. Pick the largest character from s which is smaller than the last appended
       character to the result and append it.
    6. Repeat step 5 until it is impossible to pick more characters.
    7. Repeat the steps from 1 to 6 until all the characters have been picked
       from s.

    In each step, if the smallest or the largest character appears more than
    once, choose any occurrence and append it to the result.

    Return the result string after sorting s with this algorithm.
    '''
    def sortString(self, s: str) -> str:
        result = ""
        c = Counter(s)
        l = [i for i in sorted(c.keys())]
        while len(result) < len(s):
            for a in l:
                if c[a]:
                    c[a] -= 1
                    result += a
            for a in reversed(l):
                if c[a]:
                    c[a] -= 1
                    result += a
        return result

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "aaaabbbbcccc"
        o = "abccbaabccba"
        self.assertEqual(s.sortString(i), o)

    def test_two(self):
        s = Solution()
        i = "rat"
        o = "art"
        self.assertEqual(s.sortString(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)