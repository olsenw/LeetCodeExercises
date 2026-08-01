# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string word that consists of digits and lowercase English letters.

    Replace every non-digit character with a space.

    Return the number of different integers after performing the replacement
    operations on word.

    Two integers are considered different if their decimal representations
    without any leading zeros are different.
    '''
    def numDifferentIntegers(self, word: str) -> int:
        word = "".join(w if w.isdigit() else " " for w in word)
        word = word.split()
        word = set(int(w) for w in word)
        return len(word)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "a123bc34d8ef34"
        o = 3
        self.assertEqual(s.numDifferentIntegers(i), o)

    def test_two(self):
        s = Solution()
        i = "leet1234code234"
        o = 2
        self.assertEqual(s.numDifferentIntegers(i), o)

    def test_three(self):
        s = Solution()
        i = "a1b01c001"
        o = 1
        self.assertEqual(s.numDifferentIntegers(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)