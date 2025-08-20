# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    There is an undirected tree with n nodes labeled from 0 to n - 1, and rooted
    at node 0. Given a 2D integer array edges of length n - 1, where
    edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi
    in the tree.

    A node is good if all the subtrees rooted at its children have the same
    size.

    Return the number of good nodes in the given tree.

    A subtree of treeName is a tree consisting of a node in treeName and all of
    its descendants.
    '''
    def countGoodNodes_fails(self, edges: List[List[int]]) -> int:
        answer = 0
        graph = {i:set() for i in range(len(edges) + 1)}
        for i,j in edges:
            graph[i].add(j)
            graph[j].add(i)
        def dfs(node:int, parent:int) -> int:
            nonlocal answer
            c = Counter()
            for i in graph[node]:
                if i == parent:
                    continue
                c[dfs(i, node)] += 1
            if len(c) == 0:
                answer += 1
                return 1
            s = 1
            for i in c:
                s += i * c[i]
                if c[i] > 1:
                    answer += c[i]
            return s
        dfs(0, -1)
        return answer

    def countGoodNodes(self, edges: List[List[int]]) -> int:
        graph = {i:set() for i in range(len(edges)+1)}
        for i,j in edges:
            graph[i].add(j)
            graph[j].add(i)
        answer = 0
        def dfs(node:int, last:int) -> int:
            nonlocal answer
            c = Counter()
            size = 1
            for i in graph[node]:
                if i == last:
                    continue
                s = dfs(i, node)
                size += s
                c[s] += 1
            if len(c) < 2:
                answer += 1
            return size
        dfs(0,-1)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]
        o = 7
        self.assertEqual(s.countGoodNodes(i), o)

    def test_two(self):
        s = Solution()
        i = [[0,1],[1,2],[2,3],[3,4],[0,5],[1,6],[2,7],[3,8]]
        o = 6
        self.assertEqual(s.countGoodNodes(i), o)

    def test_three(self):
        s = Solution()
        i =[[0,1],[1,2],[1,3],[1,4],[0,5],[5,6],[6,7],[7,8],[0,9],[9,10],[9,12],[10,11]]
        o = 12
        self.assertEqual(s.countGoodNodes(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)