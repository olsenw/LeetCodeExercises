# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Alice and Bob are playing a game. Initially, Alice has a string word = 'a'.

    Given a positive integer k.

    Now Bob will ask Alice to perform the following operation forever:
    * Generate a new string by changing each character in word to its next
      character in the English alphabet, and append it to the original word.
    
    Return the value of the kth character in word, after enough operations have
    been done for word to have at least k characters.

    Note that the character 'z' can be changed to 'a' in the operation.
    '''
    def kthCharacter(self, k: int) -> str:
        s = "a"
        while len(s) < k:
            i = len(s)
            for j in range(i):
                c = ord(s[j]) + 1
                s += chr(c) if c < 123 else 'a'
            pass
        return s[k-1]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 5
        o = "b"
        self.assertEqual(s.kthCharacter(i), o)

    def test_two(self):
        s = Solution()
        i = 10
        o = "c"
        self.assertEqual(s.kthCharacter(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)