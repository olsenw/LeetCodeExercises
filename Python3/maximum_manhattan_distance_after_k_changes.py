# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional, Tuple

class Solution:
    '''
    Given a string s consisting of the characters 'N', 'S', 'E', and 'W', where
    s[i] indicates movements in an infinite grid:
    * 'N': Move north by 1 unit.
    * 'S': Move south by 1 unit.
    * 'E': Move east by 1 unit.
    * 'W': Move west by 1 unit.

    Initially, start at the origin (0,0). It is possible to change at most k
    characters to any of the four directions.

    Find the maximum Manhattan distance from the origin that can be achieved at
    any time while performing the movements in order.

    The Manhattan Distance between two cells (xi, yi) and (xj, yj) is
    abs(xi - xj) + abs(yi - yj).
    '''
    def maxDistance_incomplete(self, s: str, k: int) -> int:
        def manhattan(x:int,y:int,a:int=0,b:int=0) -> int:
            return abs(x - a) + abs(y - b)
        answer = 0
        x,y = 0,0
        north, south, east, west = 0,0,0,0
        for c in s:
            if c == 'N':
                north += 1
            if c == 'S':
                south += 1
            if c == 'E':
                east += 1
            if c == 'W':
                west += 1
            # farther North than South
            if north > south:
                # farther East than West
                if east > west:
                    # Farther North than East
                    if north > east:
                        a = min(south, k)
                        b = min(west, k - a)
                        m = manhattan(north - south + a, east - west + b)
                        answer = max(answer, m)
                    # Farther East than North
                    else:
                        a = min(west, k)
                        b = min(south, k - a)
                        m = manhattan(north - south + b, east - west + a)
                        answer = max(answer, m)
                # farther West than East
                else:
                    # farther North than West
                    if north > west:
                        a = min(south, k)
                        b = min(east, k - a)
                        m = manhattan(north - south + a, east - west + b)
                        answer = max(answer, m)
                    # farther West than North
                    else:
                        a = min(west, k)
                        b = min(south, k - a)
                        m = manhattan(north - south + b, east - west + a)
                        answer = max(answer, m)
            # farther South than Nouth
            else:
                if east > west:
                    if south > east:
                        pass
                    else:
                        pass
                else:
                    if south > west:
                        pass
                    else:
                        pass
        return answer

    def maxDistance(self, s: str, k: int) -> int:
        def manhattan(n:int,s:int,e:int,w:int) -> int:
            return abs(n - s) + abs(e - w)
        def helper(north:int,south:int,east:int,west:int) -> int:
            answer = 0
            # NE
            a = min(south, k)
            b = min(west, k - a)
            answer = max(answer, manhattan(north + a, south - a, east + b, west - b))
            
            # NW
            a = min(south, k)
            b = min(east, k - a)
            answer = max(answer, manhattan(north + a, south - a, east - b, west + b))
            
            # SE
            a = min(north, k)
            b = min(west, k - a)
            answer = max(answer, manhattan(north - a, south + a, east + b, west - b))
            
            # SW
            a = min(north, k)
            b = min(east, k - a)
            answer = max(answer, manhattan(north - a, south + a, east - b, west + b))
            
            return answer
        answer = 0
        north, south, east, west = 0,0,0,0
        for c in s:
            if c == 'N':
                north += 1
            if c == 'S':
                south += 1
            if c == 'E':
                east += 1
            if c == 'W':
                west += 1
            answer = max(answer, helper(north,south,east,west))
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "NWSE"
        j = 1
        o = 3
        self.assertEqual(s.maxDistance(i,j), o)

    def test_two(self):
        s = Solution()
        i = "NSWWEW"
        j = 3
        o = 6
        self.assertEqual(s.maxDistance(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)