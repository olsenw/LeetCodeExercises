# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s, reverse the string according to the following rules:
    * All the characters that are not English letters remain in the same
      position.
    * All the English letters (lowercase or uppercase) should be reversed.

    Return s after reversing it.
    '''
    def reverseOnlyLetters(self, s: str) -> str:
        stack = []
        for c in s:
            if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
                stack.append(c)
        answer = ""
        for c in s:
            if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
                answer += stack.pop()
            else:
                answer += c
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "ab-cd"
        o = "dc-ba"
        self.assertEqual(s.reverseOnlyLetters(i), o)

    def test_two(self):
        s = Solution()
        i = "a-bC-dEf-ghIj"
        o = "j-Ih-gfE-dCba"
        self.assertEqual(s.reverseOnlyLetters(i), o)

    def test_three(self):
        s = Solution()
        i = "Test1ng-Leet=code-Q!"
        o = "Qedo1ct-eeLg=ntse-T!"
        self.assertEqual(s.reverseOnlyLetters(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)