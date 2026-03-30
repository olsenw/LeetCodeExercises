# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    Given two strings s1 and s2, both of length n, consisting of lowercase
    English letters.

    It is possible to apply the following operation on any of the two strings
    any number of times:
    * Choose any two indices i and j such that i < j and the difference j - i is
      even, then swap the two characters at those indices in the string.

    Return tru if it is possible to make the strings s1 and s2 equal, and false
    otherwise.
    '''
    def checkStrings(self, s1: str, s2: str) -> bool:
        countEvenS1 = Counter(s1[i] for i in range(0,len(s1),2))
        countOddS1 = Counter(s1[i] for i in range(1,len(s1),2))
        countEvenS2 = Counter(s2[i] for i in range(0,len(s2),2))
        countOddS2 = Counter(s2[i] for i in range(1,len(s2),2))
        return countEvenS1 == countEvenS2 and countOddS1 == countOddS2

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "abcdba"
        j = "cabdab"
        o = True
        self.assertEqual(s.checkStrings(i,j), o)

    def test_two(self):
        s = Solution()
        i = "abe"
        j = "bea"
        o = False
        self.assertEqual(s.checkStrings(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)