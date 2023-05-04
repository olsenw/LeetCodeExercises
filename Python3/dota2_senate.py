# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    In the world of Dota2, there are two parties: the Radiant and the Dire.

    The Dota2 senate consists of senators coming from two parties. Now the
    Senate wants to decide on a change in the Dota2 game. The voting for this
    change is a round-based procedure. In each round, each senator can exercise
    one of the two rights:
    * Ban one senator's right: A senator can make another senator lose all his
      rights in this and all the following rounds.
    * Announce the victory: If this senator found the senators who still have
      rights to vote are all from the same party, he can announce the victory
      and decide on the change in the game.
    
    Given a string senate representing each senator's party belonging. The
    character 'R' and 'D' represent the Radiant party and the Dire party. Then
    if there are n senators, the size of the given string will be n.

    The round-base procedure starts from the first senator to the last senator
    in the given order. This procedure will last until the end of voting. All
    the senators who have lost their rights will be skipped during the
    procedure.

    Suppose every senator is smart enough and will play the best strategy for
    his own party. Predict which party will finally announce the victory and
    change the Dota2 game. The output should be "Radiant" or "Dire"
    '''
    # toying with the idea but not solving it
    def predictPartyVictory_incomplete(self, senate: str) -> str:
        r,x = [],0
        d,y = [],0
        for i,s in enumerate(senate):
            if s == 'R':
                if x > 0:
                    x -= 1
                    continue
                r.append(i)
                if d:
                    d.pop()
                else:
                    y += 1
            else:
                if y > 0:
                    y -= 1
                    continue
                d.append(i)
                if r:
                    r.pop()
                else:
                    x += 1
        return "Radiant" if len(r) > len(d) else 'Dire'

    # based on two queue solution in leetcode editorial 
    # https://leetcode.com/problems/dota2-senate/editorial/
    def predictPartyVictory_4(self, senate: str) -> str:
        n = len(senate)
        rq = deque([i for i,s in enumerate(senate) if s == 'R'])
        dq = deque([i for i,s in enumerate(senate) if s == 'D'])
        while rq and dq:
            if rq[0] < dq[0]:
                rq.append(n + rq.popleft())
                dq.popleft()
            else:
                rq.popleft()
                dq.append(n + dq.popleft())
        return "Radiant" if rq else "Dire"

    # based on one queue solution in leetcode editorial 
    # https://leetcode.com/problems/dota2-senate/editorial/
    def predictPartyVictory(self, senate: str) -> str:
        r = senate.count("R")
        d = len(senate) - r
        rfloat,dfloat = 0, 0
        q = deque(senate)
        while r and d:
            p = q.popleft()
            if p == 'D':
                if dfloat:
                    dfloat -= 1
                    d -= 1
                else:
                    rfloat += 1
                    q.append('D')
            else:
                if rfloat:
                    rfloat -= 1
                    r -= 1
                else:
                    dfloat += 1
                    q.append('R')
        return "Radiant" if r else "Dire"

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "RD"
        o = "Radiant"
        self.assertEqual(s.predictPartyVictory(i), o)

    def test_two(self):
        s = Solution()
        i = "RDD"
        o = "Dire"
        self.assertEqual(s.predictPartyVictory(i), o)

    def test_three(self):
        s = Solution()
        i = "RRRRRDDDDRDDRDDDRDDRDDRDRRRDRDRDRDRDRDRDRDRDRDRRRDDDRDRDRDRDRRDRDRDDDRDRDRDRRDRDRDRDRRDRDRDRRDRDRRDRRDRDRRDRDRDRDRDRRDRDRDRDRDRRDRDRDRRDRDRDRRDRDRRRRRRDDDDDDDDDDDDDDDDDDDDDD"
        o = "Dire"
        self.assertEqual(s.predictPartyVictory(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)