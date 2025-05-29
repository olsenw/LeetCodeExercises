# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import DefaultDict, List, Dict, Set, Optional, Tuple

class Solution:
    '''
    There exist two undirected trees with n and m nodes, labeled from [0, n-1]
    and [0, m-1], respectively.

    Given two 2D integer arrays edges1 and edges2 of lengths n-1 and m-1,
    respectively, where edges1[i] = [ai, bi] indicates that there is an edge
    between nodes ai and bi in the first tree and edges2[i] = [ui, vi] indicates
    that there is an edge between nodes ui and vi in the second tree.

    Node u in target to node v if the number of edges on the path from u to v is
    even. Note that a node is always target to itself.

    Return an array of n integers answer, where answer[i] is the maximum
    possible number of nodes that are target to node i of the first tree if a
    node in the first tree was connected to the second tree.

    Note that the queries are independent from each other. That is, for every
    query remove the edge added in the previous query before moving to the next
    query.
    '''
    # lot of repeated computation in dfs
    def maxTargetNodes_tle(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        n, m = len(edges1) + 1, len(edges2) + 1
        def makeGraph(edges: List[List[int]]) -> DefaultDict[int,Set]:
            graph: DefaultDict[int,Set] = defaultdict(set)
            for i,j in edges:
                graph[i].add(j)
                graph[j].add(i)
            return graph
        graph = makeGraph(edges2)
        @cache
        def dfs(parent:int, node:int) -> Tuple[int,int]:
            even,odd = 1,0
            for i in graph[node]:
                if i != parent:
                    e,o = dfs(node, i)
                    even += o
                    odd += e
            return even, odd
        odd = max(dfs(-1, i)[1] for i in range(m))
        graph = makeGraph(edges1)
        dfs.cache_clear()
        return [odd + dfs(-1, i)[0] for i in range(n)]

    # based on Leetcode editorial
    # https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/editorial/?envType=daily-question&envId=2025-05-29
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def dfs(node:int, parent:int, depth:int, graph:DefaultDict[int,Set], color:List[int]) -> int:
            answer = 1 - depth % 2
            color[node] = depth % 2
            for i in graph[node]:
                if parent != i:
                    answer += dfs(i, node, depth+1, graph, color)
            return answer
        def build(edges: List[List[int]], color: List[int]) -> Tuple[int,int]:
            n = len(edges) + 1
            graph = defaultdict(set)
            for i,j in edges:
                graph[i].add(j)
                graph[j].add(i)
            answer = dfs(0, -1, 0, graph, color)
            return [answer, n - answer]
        n = len(edges1) + 1
        m = len(edges2) + 1
        color1 = [0] * n
        color2 = [0] * m
        count1 = build(edges1, color1)
        count2 = build(edges2, color2)
        answer = [0] * n
        for i in range(n):
            answer[i] = count1[color1[i]] + max(count2[0], count2[1])
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[0,1],[0,2],[2,3],[2,4]]
        j = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]
        o = [8,7,7,8,8]
        self.assertEqual(s.maxTargetNodes(i,j), o)

    def test_two(self):
        s = Solution()
        i = [[0,1],[0,2],[0,3],[0,4]]
        j = [[0,1],[1,2],[2,3]]
        o = [3,6,6,6,6]
        self.assertEqual(s.maxTargetNodes(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)