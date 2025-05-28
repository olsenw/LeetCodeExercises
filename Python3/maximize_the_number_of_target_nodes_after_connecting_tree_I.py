# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict, deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import DefaultDict, List, Dict, Set, Optional

class Solution:
    '''
    There exist two undirected trees with n and m nodes, with distinct labels in
    ranges [0, n - 1] and [0, m - 1], respectively.

    Given two 2D integer arrays edges1 and edges2 of lengths n - 1 and m - 1,
    respectively, where edges[i] = [ai, bi] indicates that there is an edge
    between nodes ai and bi in the first tree and edges2[i] = [ui, vi] indicates
    that there is an edge between nodes ui and vi in the second tree. Also given
    is an integer k.

    Node u is target to node v if the number of edges on the path from u to v is 
    less than or equal to k. Note that a node is always target to itself.

    Return an array of n integers answer, where answer[i] is the maximum
    possible number of nodes target to node i of the first tree to another node
    in the second tree.

    Note that queries are independent from each other. That is, for every query
    the added edge will be removed before proceeding to the next query.
    '''
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        graph: DefaultDict[int:Set] = defaultdict(set)
        for i,j in edges2:
            graph[i].add(j)
            graph[j].add(i)
        def dfs(parent:int, node:int, depth:int) -> int:
            if depth > k:
                return 0
            if depth == k:
                return 1
            answer = 1
            for i in graph[node]:
                if i != parent:
                    answer += dfs(node, i, depth+1)
            return answer
        dfs(-1,4,1)
        pass
        possible = [dfs(-1,i,1) for i in range(len(edges2)+1)]
        p = max(possible)
        graph: DefaultDict[int:Set] = defaultdict(set)
        for i,j in edges1:
            graph[i].add(j)
            graph[j].add(i)
        return [p + dfs(-1, i, 0) for i in range(len(edges1)+1)]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[0,1],[0,2],[2,3],[2,4]]
        j = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]
        k = 2
        o = [9,7,9,8,8]
        self.assertEqual(s.maxTargetNodes(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = [[0,1],[0,2],[0,3],[0,4]]
        j = [[0,1],[1,2],[2,3]]
        k = 1
        o = [6,3,3,3,3]
        self.assertEqual(s.maxTargetNodes(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = [[2,0],[3,1],[3,2],[3,4]]
        j = [[0,3],[0,4],[2,5],[0,2],[7,0],[1,6],[1,7]]
        k = 1
        o = [3,3,4,5,3]
        self.assertEqual(s.maxTargetNodes(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)