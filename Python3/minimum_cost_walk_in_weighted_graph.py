# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There is an undirected weighted graph with n vertices labeled from 0 to n-1.

    Given the integer n and an array edges, where edges[i] = [ui, vi, wi]
    indicates that there is an edge between vertices ui and vi with weight wi.

    A walk on a graph is a sequence of vertices and edges. The walk starts and
    ends with a vertex, and each edge connects the vertex that comes before it
    and the vertex that comes after it. It's important to note that a walk may
    visit the same edge or vertex more than once.

    The cost of a walk starting at node u and ending at node v is defined as the
    bitwise AND of the weights of the edges traversed during the walk. In other
    words, if the sequence of edge weights encountered during the walk is w0,
    w1, w2, ..., wk, then the cost is calculated as w0 & w1 & w2 & ... & wk,
    where & denotes the bitwise AND operator.

    Also given is a 2D array query, where query[i] = [si, ti]. For each query,
    find the minimum cost of the walk starting at vertex si and ending at vertex
    ti. If there exists no such walk, the answer is -1.

    Return the array answer, where answer[i] denotes the minimum cost of a walk
    for query i.
    '''
    # based on Leetcode Disjoint-Set editorial
    # https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/editorial/?envType=daily-question&envId=2025-03-20
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        # -1 means node is own parent
        parent = [-1] * n
        depth = [0] * n
        cost = [-1] * n
        def union(u, v):
            x,y = find(u), find(v)
            if x == y:
                return
            if depth[x] < depth[y]:
                x,y = y,x
            parent[y] = x
            if depth[x] == depth[y]:
                depth[x] += 1
        def find(node):
            if parent[node] == -1:
                return node
            parent[node] = find(parent[node])
            return parent[node]
        # find components
        for i,j,k in edges:
            union(i, j)
        # calculate cost for each component
        for i,j,k in edges:
            root = find(i)
            cost[root] &= k
        answer = []
        for i,j in query:
            root = find(i)
            # start node and end node are in different components
            if root != find(j):
                answer.append(-1)
            # contained in same component
            else:
                answer.append(cost[root])
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 5
        j = [[0,1,7],[1,3,7],[1,2,1]]
        k = [[0,3],[3,4]]
        o = [1,-1]
        self.assertEqual(s.minimumCost(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = 3
        j = [[0,2,7],[0,1,15],[1,2,6],[1,2,1]]
        k = [[1,2]]
        o = [0]
        self.assertEqual(s.minimumCost(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)