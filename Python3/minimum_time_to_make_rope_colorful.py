# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Alice has n balloons arranged on a rope. Given an 0-indexed string colors
    where colors[i] is the color of the ith balloon.
    
    Alice wants the rope to be colorful. She does not want two consecutive
    balloons to be of the same color, so she asks Bob for help. Bob can remove
    some balloons from the rope to make it colorful. Given a 0-indexed integer
    array neededTime where neededTime[i] is the time (in seconds) that Bob needs
    to remove the ith balloon from the rope.

    Return the minimum time Bob needs to make the rope colorful.
    '''
    def minCost_slow(self, colors: str, neededTime: List[int]) -> int:
        segments = []
        last = 0
        for i in range(1, len(colors)):
            if colors[i] != colors[last]:
                segments.append((last,i))
                last = i
        segments.append((last,len(colors)))
        total = 0
        for s,e in segments:
            total += sum(neededTime[s:e]) - max(neededTime[s:e])
        return total

    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total = 0
        l,r,m = 0, neededTime[0], neededTime[0]
        for i in range(1, len(colors)):
            if colors[i] != colors[l]:
                total += r - m
                l, r, m = i, neededTime[i], neededTime[i]
            else:
                r += neededTime[i]
                m = max(m, neededTime[i])
        return total + r - m

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "abaac"
        j = [1,2,3,4,5]
        o = 3
        self.assertEqual(s.minCost(i,j), o)

    def test_two(self):
        s = Solution()
        i = "abc"
        j = [1,2,3]
        o = 0
        self.assertEqual(s.minCost(i,j), o)

    def test_three(self):
        s = Solution()
        i = "aabaa"
        j = [1,2,3,4,1]
        o = 2
        self.assertEqual(s.minCost(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)