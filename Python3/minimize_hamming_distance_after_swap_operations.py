# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter, defaultdict
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two integer arrays, source and target, both of length n. Also given an
    array allowedSwaps where each allowedSwaps[i] = [ai, bi] indicates that it
    is possible to swap the elements at index ai and index bi (0-indexed) of
    array source. Note that it is possible elements at a specific pair of
    indices multiple times and in any order.

    The hamming distance of two arrays of the same length, source and target, is
    the number of positions where the elements are different. Formally, it is
    the number of indices i for 0 <= i <= n-1 where sources[i] != target[i]
    (0-indexed).

    Return the minimum Hamming distance of source and target after performing
    any amount of swap operations on array source.
    '''
    # looked up geeks for geeks union-find
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        parent = [i for i in range(n)]
        def find(node:int) -> int:
            # if node == parent[node] then it is a representative node of set
            if node == parent[node]:
                return node
            # recursively find parent
            return find(parent[node])
        def uniion(a:int,b:int) -> None:
            # find representative of set containing a
            ap = find(a)
            # find representative of set containing a
            bp = find(b)
            # make set b be part of set a
            parent[bp] = ap
        for a,b in allowedSwaps:
            uniion(a,b)
        d = defaultdict(Counter)
        for i,j in enumerate(source):
            d[find(i)][j] += 1
        hamming = 0
        for i,j in enumerate(target):
            i = find(i)
            if d[i][j] > 0:
                d[i][j] -= 1
            else:
                hamming += 1
        return hamming

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,4]
        j = [2,1,4,5]
        k = [[0,1],[2,3]]
        o = 1
        self.assertEqual(s.minimumHammingDistance(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,4]
        j = [1,3,2,4]
        k = []
        o = 2
        self.assertEqual(s.minimumHammingDistance(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = [5,1,2,4,3]
        j = [1,5,4,2,3]
        k = [[0,4],[4,2],[1,3],[1,4]]
        o = 0
        self.assertEqual(s.minimumHammingDistance(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)