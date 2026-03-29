# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two strings s1 and s2, both of length 4, consisting of lowercase
    English letters.

    The following operation can be performed on any of the two strings any
    number of times:
    * Choose any two indices i and j such that j - i = 2, then swap the two
      characters at those indices in the string.
    
    Return true if it is possible to make the strings s1 and s2 equal, and false
    otherwise.
    '''
    def canBeEqual(self, s1: str, s2: str) -> bool:
        def makeGroup(s:str) -> Set[str]:
            group = {
                s,
                "".join([s[2],s[1],s[0],s[3]]),
                "".join([s[0],s[3],s[2],s[1]]),
            }
            return group
        group1 = makeGroup(s1)
        group2 = makeGroup(s2)
        return any(w in group2 for w in group1)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "abcd"
        j = "cdab"
        o = True
        self.assertEqual(s.canBeEqual(i,j), o)

    def test_two(self):
        s = Solution()
        i = "abcd"
        j = "dacb"
        o = False
        self.assertEqual(s.canBeEqual(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)