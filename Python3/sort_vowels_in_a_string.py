# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed string s, permute s to get a new string t such that:
    * All consonants remain in their original places. More formally, if there is
      an index i with 0 <= i < s.length such that s[i] is a consonant, then
      t[i] = s[i].
    * The vowels must be sorted in the nondecreasing order of their ASCII
      values. More formally, for pairs of indices i, j with
      0 <= i < j < s.length such that s[i] and s[j] are vowels, the t[i] must
      not have a higher ASCII value than t[j].
    
    Return the resulting string.

    The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in lowercase
    or uppercase. Consonants comprise all letters that are not vowels.
    '''
    def sortVowels(self, s: str) -> str:
        vowels = sorted((c for c in s if c in "AEIOUaeiou"), reverse=True)
        return ''.join(vowels.pop() if c in "AEIOUaeiou" else c for c in s)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "lEetcOde"
        o = "lEOtcede"
        self.assertEqual(s.sortVowels(i), o)

    def test_two(self):
        s = Solution()
        i = "lYmpH"
        o = "lYmpH"
        self.assertEqual(s.sortVowels(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)