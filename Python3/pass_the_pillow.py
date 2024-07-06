# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There are n people standing in a line labeled from 1 to n. The first person
    in the line is holding a pillow initially. Every second, the person holding
    the pillow passes it to the next person standing in the line. Once the
    pillow reaches the end of the line, the direction changes, and people
    continue passing the pillow in the opposite direction.

    Given the two positive integers n and time, return the index of the person
    holding the pillow after time seconds.
    '''
    def passThePillow_brute(self, n: int, time: int) -> int:
        curr = 1
        adv = 1
        while time:
            if curr == n:
                adv = -1
            curr += adv
            time -= 1
            if curr == 1:
                adv = 1
        return curr

    def passThePillow(self, n: int, time: int) -> int:
        t = time // (n - 1)
        if t % 2 == 0:
            return 1 + (time % (n-1))
        else:
            return n - (time % (n-1))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 4
        j = 5
        o = 2
        self.assertEqual(s.passThePillow(i,j), o)

    def test_two(self):
        s = Solution()
        i = 3
        j = 2
        o = 3
        self.assertEqual(s.passThePillow(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)