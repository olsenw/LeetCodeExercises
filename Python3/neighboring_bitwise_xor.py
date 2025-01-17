# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A 0-indexed array derived with length n is derived by computing the bitwise
    XOR of adjacent values in a binary array original of length of n.

    Specifically, for each index i in the range [0, n - 1]:
    * If i = n - 1, then derived[i] = original[i] XOR original[0].
    * Otherwise, derived[i] = original[i] XOR original[i + 1].

    Given an array derived, determine whether there exists a valid binary array
    original that could have formed derived.

    Return true if such an array exists of false otherwise.
    * A binary array is an array containing only 0's and 1's.
    '''
    # hints
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        answer = 0
        for i in derived:
            answer ^= i
        return answer == 0

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,1,0]
        o = True
        self.assertEqual(s.doesValidArrayExist(i), o)

    def test_two(self):
        s = Solution()
        i = [1,1]
        o = True
        self.assertEqual(s.doesValidArrayExist(i), o)

    def test_three(self):
        s = Solution()
        i = [1,0]
        o = False
        self.assertEqual(s.doesValidArrayExist(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)