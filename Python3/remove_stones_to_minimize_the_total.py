# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a 0-indexed integer array piles, where piles[i] represents the number
    of stones in the ith pile, and an integer k. The following operation is
    applied k times:
    * Choose any piles[i] and remove floor(piles[i] / 2) stones from it.

    Notice that operation may be applied to the same pile more than once.

    Return the minimum possible total number of stones remaining after applying
    the k operations.

    floor(x) is the greatest integer that is smaller than or equal to x (ie,
    rounds x down).
    '''
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-p for p in piles]
        heapq.heapify(piles)
        for _ in range(k):
            p = -piles[0]
            p = p - p // 2
            heapq.heapreplace(piles, -p)
        return -sum(piles)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [5,4,9]
        j = 2
        o = 12
        self.assertEqual(s.minStoneSum(i,j), o)

    def test_two(self):
        s = Solution()
        i = [4,3,6,7]
        j = 3
        o = 12
        self.assertEqual(s.minStoneSum(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)