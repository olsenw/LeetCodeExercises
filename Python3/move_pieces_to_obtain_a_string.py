# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two strings start and target, both of length n. Each string consists
    only of the character 'L', 'R', and '_' where:
    * The characters 'L' and 'R' represent pieces, where a piece 'L' can move to
      the left only if there is a blank space directly to its left, and a piece
      'R' can move to the right only if there is a blank space directly to it
      right.
    * The character '_' represents a blank space that can be occupied by any of
      the 'L' or 'R' pieces.
    
    Return true if it is possible to obtain the string target by moving the
    pieces of the string start any number of times. Otherwise, return false.
    '''
    def canChange(self, start: str, target: str) -> bool:
        r = 0
        j = 0
        for i in range(len(target)):
            if target[i] == 'L':
                while j < len(start) and start[j] != 'L':
                    if start[j] == 'R':
                        r += 1
                    j += 1
                if j == len(start) or j < i or r > 0:
                    return False
                j += 1
            if target[i] == 'R':
                while j < i and start[j] != 'R':
                    if start[j] == 'L':
                        return False
                    j += 1
                if start[j] != 'R':
                    return False
                j += 1
        while j < len(start):
            if start[j] != '_':
                return False
            j += 1
        return True

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "_L__R__R_", "L______RR"
        o = True
        self.assertEqual(s.canChange(*i), o)

    def test_two(self):
        s = Solution()
        i = "R_L_", "__LR"
        o = False
        self.assertEqual(s.canChange(*i), o)

    def test_three(self):
        s = Solution()
        i = "_R", "R_"
        o = False
        self.assertEqual(s.canChange(*i), o)

    def test_four(self):
        s = Solution()
        i = "_LL__R__R_", "L___L___RR"
        o = False
        self.assertEqual(s.canChange(*i), o)

    def test_five(self):
        s = Solution()
        i = "_L__R__R_L", "L______RR_"
        o = False
        self.assertEqual(s.canChange(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)