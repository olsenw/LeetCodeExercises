# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

import heapq

class node:
    def __init__(self, letter) -> None:
        self.letter= letter
        # self.children = set()
        self.children = []

class Solution:
    '''
    Given a tree (ie a connected undirected graph that has no cycles) rooted at
    node 0 consisting of n nodes numbered from 0 to n - 1. The tree is
    represented by a 0-indexed array parent of size n, where parent[i] is the
    parent of node i. Since node 0 is the root parent[0] == -1.

    Also given a string s of length n, where s[i] is the character assigned to
    node i.

    Return the length of the longest path in the tree such that no pair of
    adjacent nodes on the path have the same character assigned to them.
    '''
    def longestPath(self, parent: List[int], s: str) -> int:
        answer = 0
        t = {i:node(s[i]) for i in range(len(s))}
        for i,p in enumerate(parent[1:], 1):
            # t[p].children.add(t[i])
            t[p].children.append(t[i])
        def dfs(n:node, c:str) -> int:
            nonlocal answer
            if len(n.children) == 0:
                answer = max(answer, 1)
                return 0 if c == n.letter else 1
            if len(n.children) == 1:
                a = dfs(n.children[0], n.letter)
                answer = max(answer, 1 + a)
                return 0 if c == n.letter else 1 + a
            a = []
            for i in n.children:
                if len(a) == 2:
                    heapq.heappushpop(a, dfs(i, n.letter))
                else:
                    heapq.heappush(a, dfs(i, n.letter))
            answer = max(answer, 1 + a[0] + a[1])
            return 0 if c == n.letter else 1 + a[1]
        dfs(t[0], t[0].letter)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [-1,0,0,1,1,2]
        j = "abacbe"
        o = 3
        self.assertEqual(s.longestPath(i,j), o)

    def test_two(self):
        s = Solution()
        i = [-1,0,0,0]
        j = "aabc"
        o = 3
        self.assertEqual(s.longestPath(i,j), o)

    def test_three(self):
        s = Solution()
        i = [-1,0,0,2]
        j = "abbc"
        o = 4
        self.assertEqual(s.longestPath(i,j), o)

    def test_four(self):
        s = Solution()
        i = [-1,0,0,2,3,4]
        j = "abacbb"
        o = 3
        self.assertEqual(s.longestPath(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)