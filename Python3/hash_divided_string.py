# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s of length n and an integer k, where n is a multiple of k.
    Hash the string s into a new string called result, which has a length of
    n / k.

    First divide s into n / k substrings each with a length of k. Then,
    initialize result as an empty string.

    For each substring in order from the beginning:
    * The hash value of a character is the index of that character in the
      English alphabet ('a' -> 0, ..., 'z' -> 25).
    * Calculate the sum of all the hash values of the characters in the
      substring
    * Find the remainder of this sum when divided by 26, which is called
      hashedChar.
    * Identify the character in the English lowercase alphabet that corresponds
      to hashChar.
    * Append that character to the end of result.

    Return result.
    '''
    def stringHash(self, s: str, k: int) -> str:
        answer = ""
        for i in range(0, len(s), k):
            a = 0
            for j in range(i, i + k):
                a += ord(s[j]) - 97
            answer += chr((a % 26) + 97)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "abcd"
        j = 2
        o = "bf"
        self.assertEqual(s.stringHash(i,j), o)

    def test_two(self):
        s = Solution()
        i = "mxz"
        j = 3
        o = "i"
        self.assertEqual(s.stringHash(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)