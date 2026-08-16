# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Alice and Bob continue their games with stones. There is a row of n stones,
    and each stone has an associated value. Also given an integer array stones,
    where stones[i] is the value of the ith stone.

    Alice and Bob take turns, with Alice starting first. On each turn, the
    player may remove any stone from stones. The player who removes a stone
    loses if the sum of the values of all removed stones is divisible by 3. Bob
    will win automatically if there are no remaining stones (even if it is
    Alice's turn).

    Assuming both players play optimally, return true if Alice wins and false if
    Bob wins.
    '''
    def stoneGameIX_tle(self, stones: List[int]) -> bool:
        values = [0] * 3
        for s in stones:
            values[s % 3] += 1
        def alice(remainder:int) -> bool:
            if remainder == 0:
                return True
            if all(v == 0 for v in values):
                return 
            win = False
            for v in range(3):
                if values[v] == 0:
                    continue
                values[v] -= 1
                if not bob((remainder + v) % 3):
                    win = True
                values[v] += 1
            return win
        def bob(remainder:int) -> bool:
            if remainder == 0:
                return True
            if all(v == 0 for v in values):
                return True
            win = False
            for v in range(3):
                if values[v] == 0:
                    continue
                values[v] -= 1
                if not alice((remainder + v) % 3):
                    win = True
                values[v] += 1
            return win
        if values[1] > 0:
            values[1] -= 1
            if not bob(1):
                return True
            values[1] += 1
        if values[2] > 0:
            values[2] -= 1
            if not bob(2):
                return True
            values[2] += 1
        return False

    # based on leetcode solution
    # https://leetcode.com/problems/stone-game-ix/editorial/?envType=daily-question&envId=2026-08-16
    # stone with a remainder of 0 (stone % 3) flip turns and delay
    #     possible for this to cause Alice to loose if last stone
    # otherwise only two possible patterns for taking stones
    #     11212121212...
    #     22121212121...
    def stoneGameIX(self, stones: List[int]) -> bool:
        values = [0] * 3
        for s in stones:
            values[s % 3] += 1
        zeros, ones, twos = values[0], values[1], values[2]
        # There is an even number of turn flips (no change in order possible)
        if zeros % 2 == 0:
            # if there is one Ones stone and one Twos stone Alice must win
            return ones >= 1 and twos >= 1
        # There is an odd number of turn flips (Alice may loose by removing last stone)
        # Alice only wins if Bob would have won without Zero stones
        # This is only possible when Ones/Twos are 2+ greater than other
        return ones - twos > 2 or twos - ones > 2

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,1]
        o = True
        self.assertEqual(s.stoneGameIX(i), o)

    def test_two(self):
        s = Solution()
        i = [2]
        o = False
        self.assertEqual(s.stoneGameIX(i), o)

    def test_three(self):
        s = Solution()
        i = [5,1,2,4,3]
        o = False
        self.assertEqual(s.stoneGameIX(i), o)

    def test_four(self):
        s = Solution()
        i = [1] * (10**5)
        o = False
        self.assertEqual(s.stoneGameIX(i), o)

    def test_five(self):
        s = Solution()
        i = [77,74,12,63,95,23,19,91,48,87,26,22,21,30,41,10,22,80,14,36,62,29,13,3,15,47,71,1,95,21,43,84,62,70,10,86,70,9,38,30,51,32,75,87,73,8,54,64,35,22,68,75,4,59,69,82,27,9,20,32,64,59,58,48,32,21,15,20,75]
        o = True
        self.assertEqual(s.stoneGameIX(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)