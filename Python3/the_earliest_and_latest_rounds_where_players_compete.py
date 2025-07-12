# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There is a tournament where n players are participating. The players are
    standing in a single row and are numbered from 1 to  based on their initial
    standing position (player 1 is the first player in the row, player 2 is the
    second player in the row, etc).

    The tournament consists of multiple rounds (starting from round number 1).
    In each round, the ith player from the front of row competes against the ith
    player from the end of the row, and the winner advances to the next round.
    When the number is players is odd for the current round, the player in the
    middle automatically advances to the next round.

    After each round is over, the winners are lined back up in the row based on
    the original ordering assigned to them initially (ascending order).

    The players numbered firstPlayer and secondPlayer are the best in the
    tournament. They can win against any other player before they complete
    against each other. If any two other players compete against each other,
    either of them might win.

    Given the integers n, firstPlayer, and second Player, return an integer
    array containing two values, the earliest possible round number and the
    latest possible round number in which these two players will compete against
    each other, respectively.
    '''
    def earliestAndLatest_unfocused(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        '''
        use dp to calculate the depth of rounds
        use backtracking to generate all the outcomes of a given round
        '''
        def outcome(players:str) -> List[str]:
            return
        @cache
        def dp(players:str) -> int:
            small, large = 10**9 + 7, 0
            possible = []
            for i in range(n):
                pass
            return [small, large]
        return dp("1" * n)

    # try to generate all states from given state
    def earliestAndLatest_fails(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        firstPlayer -= 1
        secondPlayer -= 1
        @cache
        def dp(state:int):
            small,large = 10**5, 0
            backtrack = [(state,0,n-1)]
            while backtrack:
                state,i,j = backtrack.pop()
                pass
                while i < n and ((1 << i) & state) == 0:
                    i += 1
                while j > -1 and ((1 << j) & state) == 0:
                    j -= 1
                if i < j:
                    if i == firstPlayer and j == secondPlayer:
                        return [0,0]
                    elif i == firstPlayer:
                        backtrack.append((state ^ (1 << j), i+1, j-1))
                        pass
                    elif j == secondPlayer:
                        backtrack.append((state ^ (1 << i), i+1, j-1))
                        pass
                    else:
                        backtrack.append((state ^ (1 << i), i+1, j-1))
                        backtrack.append((state ^ (1 << j), i+1, j-1))
                        pass
                # elif i == j:
                #     backtrack.append((state & (1 << i), i+1, j-1))
                else:
                    s,l = dp(state)
                    small = min(small, 1 + s)
                    large = max(large, 1 + l)
            return [small, large]
        # round zero with all participants
        return [i+1 for i in dp((1 << n) - 1)]

    # based on leetcode editorial
    # https://leetcode.com/problems/the-earliest-and-latest-rounds-where-players-compete/?envType=daily-question&envId=2025-07-12
    # state transitions are magic...
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        @cache
        def dp(n:int, f:int, s:int) -> List[int]:
            if f + s == n + 1:
                return [1,1]
            # F(n,f,s) == F(n,n+1-s,n+1-f)
            if f + s > n + 1:
                return dp(n, n + 1 - s, n + 1 - f)
            a,b = float('inf'), float('-inf')
            nhalf = (n+1) // 2
            if s <= nhalf:
                # s on left or middle
                for i in range(f):
                    for j in range(s-f):
                        x,y = dp(nhalf, i+1, i+j+2)
                        a = min(a, x)
                        b = max(b, y)
            else:
                # s on the right
                s = n + 1 - s
                mid = (n - 2 * s + 1) // 2
                for i in range(f):
                    for j in range(s - f):
                        x,y = dp(nhalf, i + 1, i + j + mid + 2)
                        a = min(a, x)
                        b = max(b, y)
            return [a+1,b+1]
        return dp(n, firstPlayer, secondPlayer)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 11
        j = 2
        k = 4
        o = [3,4]
        self.assertEqual(s.earliestAndLatest(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = 5
        j = 1
        k = 5 
        o = [1,1]
        self.assertEqual(s.earliestAndLatest(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = 3
        j = 1
        k = 2 
        o = [2,2]
        self.assertEqual(s.earliestAndLatest(i,j,k), o)

    def test_four(self):
        s = Solution()
        i = 3
        j = 2
        k = 3 
        o = [2,2]
        self.assertEqual(s.earliestAndLatest(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)