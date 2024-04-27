# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    In the video game Fallout 4, the quest "Road ti Freedom" requires players to
    reach a metal dial called the "Freedom Trail Ring" and use the dial to spell
    a specific keyword to open the door.

    Given a string ring that represents the code engraved on the outer ring and
    another string key that represents the keyword that needs to be spelled,
    return the minimum number of steps to spell all the characters in the
    keyword.

    Initially, the first character of the ring is aligned at the "12:00"
    direction. Spell all the characters in key one by one by rotating ring
    clockwise or anticlockwise to make each character of the string key aligned
    at the "12:00" direction and then by pressing the center button.

    At the stage of rotating the ring to spell the key character key[i]:
    1. Possible to rotate the ring clockwise or anticlockwise by one place,
       which counts as one step. The final purpose of the rotation is to align
       one of ring's characters at the "12:00" direction where this character
       must equal key[i].
    2. If the character key[i] has been aligned at the "12:00" direction, press
       the center button to spell, which also counts as one step. After the
       pressing, it is possible to begin spell the next character in the key
       (next stage). Otherwise the spelling has finished.
    '''
    def findRotateSteps_time_limit_exceeded(self, ring: str, key: str) -> int:
        m,n = len(ring), len(key)
        @cache
        def dfs(index,target):
            if target == n:
                return 0
            answer = 100000
            for i in range(-m,m):
                j = (index + i) % m
                if ring[j] == key[target]:
                    answer = min(answer, abs(i) + dfs(j, target + 1))
                    pass
            return answer
        return dfs(0,0) + n

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "godding"
        j = "gd"
        o = 4
        self.assertEqual(s.findRotateSteps(i,j), o)

    def test_two(self):
        s = Solution()
        i = "godding"
        j = "godding"
        o = 13
        self.assertEqual(s.findRotateSteps(i,j), o)

    def test_three(self):
        s = Solution()
        i = "abcdefghijklmnopqrstuvwxyz"
        j = "twentytwothingstocheckout"
        o = 168
        self.assertEqual(s.findRotateSteps(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)