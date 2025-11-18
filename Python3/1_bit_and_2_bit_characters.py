# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There are two special characters:
    * The first character can be represented by one bit 0.
    * The second character can be represented by two bits (10 or 11).

    Given a binary array bits that ends with 0, return true if the last
    character must be a one-bit character.
    '''
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        while i < len(bits) - 1:
            if bits[i] == 1:
                i += 1
            i += 1
        return i < len(bits)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,0,0]
        o = True
        self.assertEqual(s.isOneBitCharacter(i), o)

    def test_two(self):
        s = Solution()
        i = [1,1,1,0]
        o = False
        self.assertEqual(s.isOneBitCharacter(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)