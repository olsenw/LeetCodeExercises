# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a string s, reverse only all the vowels in the string and return it.

    The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both
    lower and upper cases, more than once. 
    '''
    def reverseVowels(self, s: str) -> str:
        vowels = [c for c in s if c in "aAeEiIoOuU"]
        answer = ''
        for c in s:
            answer += vowels.pop() if c in 'aAeEiIoOuU' else c
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "hello"
        o = "holle"
        self.assertEqual(s.reverseVowels(i), o)

    def test_two(self):
        s = Solution()
        i = "leetcode"
        o = "leotcede"
        self.assertEqual(s.reverseVowels(i), o)

    def test_three(self):
        s = Solution()
        i = "aA"
        o = "Aa"
        self.assertEqual(s.reverseVowels(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)