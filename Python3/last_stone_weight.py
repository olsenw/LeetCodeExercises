# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

import heapq

class Solution:
    '''
    Given an array of integers stones where stones[i] is the weight of 
    the ith stone.

    A game is played with these stones. On each turn, the two heaviest
    stones are smashed together. Suppose the heaviest two stones have
    weights x and y with x <= y. The result of this smash is:
    * If x == y, both stones are destroyed.
    * If x != y, the stone of weight x is destroyed, and the stone of
      weight y has new weight y - x.

    At the end of the game, there is at most one stone left.

    Return the smallest possible weight of the left stone. If there are
    no stones left return 0.
    '''
    def lastStoneWeight(self, stones: List[int]) -> int:
        s = [-s for s in stones]
        heapq.heapify(s)
        while len(s) > 1:
            x = heapq.heappop(s)
            # both stones destroyed
            if s[0] == x:
                heapq.heappop(s)
            # stone y destroyed x is damaged
            else:
                heapq.heapreplace(s, x - s[0])
        return -s[0] if s else 0

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,7,4,1,8,1]
        o = 1
        self.assertEqual(s.lastStoneWeight(i), o)

    def test_two(self):
        s = Solution()
        i = [1]
        o = 1
        self.assertEqual(s.lastStoneWeight(i), o)

    def test_three(self):
        s = Solution()
        i = [1,1]
        o = 0
        self.assertEqual(s.lastStoneWeight(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)