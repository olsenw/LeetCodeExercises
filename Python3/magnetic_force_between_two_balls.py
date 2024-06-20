# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import bisect
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    In the universe Earth C-137, Rick discovered a special form of magnetic
    force between two balls if they are put in his newly invented basket. Rick
    has n empty baskets, the ith basket is at position[i], Morty has m balls and
    needs to distribute the balls into the baskets such that the minimum
    magnetic force between any two balls is maximum.

    Rick stated that magnetic force between two different balls at positions x
    and y is |x-y|.

    Given the integer array position and the integer m. Return the required
    force.
    '''
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def test(distance):
            c = 1
            l = position[0]
            for p in position:
                if p - l >= distance:
                    c += 1
                    l = p
            return c >= m
        a = 0
        i,j = 1, position[-1] - position[0]
        while i <= j:
            k = i + (j - i) // 2
            if test(k):
                a = k
                i = k + 1
            else:
                j = k - 1
        return a

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,4,7]
        j = 3
        o = 3
        self.assertEqual(s.maxDistance(i,j), o)

    def test_two(self):
        s = Solution()
        i = [5,4,3,2,1,1000000000]
        j = 2
        o = 999999999
        self.assertEqual(s.maxDistance(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)