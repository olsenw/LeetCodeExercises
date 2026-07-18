# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s and an integer k. Encrypt the string using the following
    algorithm.
    * For each character c in s, replace c with the kth character after c in the
      string (in a cyclic manner).
    
    Return the encrypted string.
    '''
    def getEncryptedString(self, s: str, k: int) -> str:
        n = len(s)
        return "".join(s[(i+k) % n] for i in range(n))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "dart"
        j = 3
        o = "tdar"
        self.assertEqual(s.getEncryptedString(i,j), o)

    def test_two(self):
        s = Solution()
        i = "aaa"
        j = 1
        o = "aaa"
        self.assertEqual(s.getEncryptedString(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)