# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There s a group of n people labeled from 0 to n - 1 where each person has a
    different amount of money and a different level of quietness.

    Given an array richer where richer[i] = [ai, bi] indicates that ai has more
    money than bi and an integer array quiet where quiet[i] is the quietness of
    the ith person. All the given data in richer are logically correct (i.e, the
    data will not lead to a situation where x is richer than y and y is richer
    than x at the same time).

    Return an integer array answer where answer[x] = y if y is the least quiet
    person (that is, the person y with the smallest value of quiet[y]) among all
    people who definitely have equal to or more money than the person x.
    '''
    def loudAndRich(self, richer: list[list[int]], quiet: list[int]) -> list[int]:
        graph = defaultdict(list)
        for i,j in richer:
            graph[j].append(i)
        @cache
        def dfs(node:int) -> int:
            n,q = node, quiet[node]
            for i in graph[node]:
                j,k = dfs(i)
                if k < q:
                    n,q = j,k
            return [n,q]
        return [dfs(i)[0] for i in range(len(quiet))]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]]
        j = [3,2,5,4,6,1,7,0]
        o = [5,5,2,5,4,5,6,7]
        self.assertEqual(s.loudAndRich(i,j), o)

    def test_two(self):
        s = Solution()
        i = []
        j = [0]
        o = [0]
        self.assertEqual(s.loudAndRich(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)