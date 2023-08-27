# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A frog is crossing a river. The river is divided into some number of units,
    and at each unit, there may or may not exist a stone. The frog can jump on a
    stone, but it must not jump into the water.

    Given a list of stones positions (in units) in sorted ascending order,
    determine if the frog can cross the river by landing on the last stone.
    Initially, the frog is on the first stone and assumes the first jump must be
    1 unit.

    If the frog's last jump was k units, its next jump must be either k-1, k, or
    k+1 units. The frog can only jump in the forward direction.
    '''
    def canCross_passes(self, stones: List[int]) -> bool:
        n = len(stones)
        @cache
        def dp(i, k):
            if i == n - 1:
                return True
            possible = False
            j = i + 1
            # k-1
            while j < n and stones[j] < stones[i] + k - 1:
                j += 1
            if j < n and stones[j] == stones[i] + k - 1:
                possible |= dp(j, k - 1)
            # k
            while j < n and stones[j] < stones[i] + k:
                j += 1
            if j < n and stones[j] == stones[i] + k:
                possible |= dp(j, k)
            # k+1
            while j < n and stones[j] < stones[i] + k + 1:
                j += 1
            if j < n and stones[j] == stones[i] + k + 1:
                possible |= dp(j, k + 1)
            return possible
        return dp(0,0)

    # looking at other solutions and noticed the use of set
    def canCross(self, stones: List[int]) -> bool:
        target = stones[-1]
        stones = set(stones)
        @cache
        def dp(i, k):
            if i == target:
                return True
            possible = False
            for j in [k-1, k, k+1]:
                stone = i + j
                if j > 0 and stone in stones:
                    possible |= dp(stone, j)
            return possible
        return dp(0,0)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [0,1,3,5,6,8,12,17]
        o = True
        self.assertEqual(s.canCross(i), o)

    def test_two(self):
        s = Solution()
        i = [0,1,2,3,4,8,9,11]
        o = False
        self.assertEqual(s.canCross(i), o)

    def test_three(self):
        s = Solution()
        i = [0,1]
        o = True
        self.assertEqual(s.canCross(i), o)

    def test_four(self):
        s = Solution()
        i = [0,2]
        o = False
        self.assertEqual(s.canCross(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)