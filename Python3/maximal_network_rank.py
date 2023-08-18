# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There is an infrastructure of n cities with some number of roads connecting
    these cities. Each roads[i] = [ai, bi] indicates that there is a
    bidirectional road between cites ai and bi.

    The network rank of two different cities is defined as the total number of
    directly connected roads to either city. If a road is directly connected to
    both cities, it is only counted once.

    The maximal network rank of the infrastructure is the maximum rank of all
    pairs of different cities.

    Given the integer n and the array roads, return the maximal network rank of
    the entire infrastructure.
    '''
    # little brute force... could find the in-degree better
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        r = defaultdict(set)
        for i,(a,b) in enumerate(roads):
            r[a].add(i)
            r[b].add(i)
        return max(len(r[i].union(r[j])) for i in range(n) for j in range(i+1, n))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 4
        j = [[0,1],[0,3],[1,2],[1,3]]
        o = 4
        self.assertEqual(s.maximalNetworkRank(i,j), o)

    def test_two(self):
        s = Solution()
        i = 5
        j = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
        o = 5
        self.assertEqual(s.maximalNetworkRank(i,j), o)

    def test_three(self):
        s = Solution()
        i = 8
        j = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
        o = 5
        self.assertEqual(s.maximalNetworkRank(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)