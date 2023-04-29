# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

# Leetcode union find
# https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/editorial/
class UnionFind:
    def __init__(self, size: int):
        self.group = [0] * size
        self.rank = [0] * size
        for i in range(size):
            self.group[i] = i

    def find(self, node: int) -> int:
        if self.group[node] != node:
            self.group[node] = self.find(self.group[node])
        return self.group[node]

    def join(self, node1: int, node2: int):
        group1 = self.find(node1)
        group2 = self.find(node2)
        
        # node1 and node2 already belong to same group.
        if group1 == group2:
            return

        if self.rank[group1] > self.rank[group2]:
            self.group[group2] = group1
        elif self.rank[group1] < self.rank[group2]:
            self.group[group1] = group2
        else:
            self.group[group1] = group2
            self.rank[group2] += 1
    
    def are_connected(self, node1: int, node2: int) -> bool:
        return self.find(node1) == self.find(node2)

class Solution:
    '''
    An undirected graph of n nodes is defined by edgeList, where
    edgeList[i] = [ui, vi, disi] denotes an edge between nodes ui and vi with
    distance disi. Note that there may be multiple edges between two nodes.

    Given an array queries, where queries[j] = [pj, qj, limitj], determine for
    each queries[j] whether there is a path between pj and qj such that each
    edge on the path has a distance strictly less than limitj.

    Return a boolean array answer, where answer.length == queries.length and the
    jth value of answer is true if there is a path for queries[j] is true, and
    false otherwise.
    '''
    # time limit exceeded (15/23 test cases)
    def distanceLimitedPathsExist_tle(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # edgeList.sort(key=lambda x: (x[0], x[2], x[1]))
        graph = {i:[] for i in range(n)}
        for a,b,c in edgeList:
            graph[a].append((b,c))
            graph[b].append((a,c))
        for i in range(n):
            graph[i].sort()
        def bfs(start,end,limit):
            v = set()
            q = deque([start])
            while q:
                n = q.popleft()
                if n in v:
                    continue
                if n == end:
                    return True
                v.add(n)
                for i,j in graph[n]:
                    if j < limit:
                        q.append(i)
            return False
        return [bfs(a,b,c) for a,b,c in queries]

    # time limit exceeded (but a little faster...)
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = {i:[] for i in range(n)}
        @cache
        def bfs(start,end):
            q = deque([start])
            v = set()
            while q:
                n = q.popleft()
                if n in v:
                    continue
                if n == end:
                    return True
                v.add(n)
                for i in graph[n]:
                    q.append(i)
            return False
        edgeList.sort(key=lambda x:(x[2],x[0],x[1]))
        eIndex = 0
        queries = sorted(enumerate(queries), key=lambda x:(x[1][2],x[1][0],x[1][1],x[0]))
        # queries.sort(key=lambda x:(x[2],x[0],x[1]))
        answer = []
        for a,(b,c,d) in queries:
            while eIndex < len(edgeList) and edgeList[eIndex][2] < d:
                i,j,_ = edgeList[eIndex]
                graph[i].append(j)
                graph[j].append(i)
                eIndex += 1
            answer.append((a,bfs(b,c)))
        return [j for i,j in sorted(answer)]

    # Leetcode union find solution
    # https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/editorial/
    def distanceLimitedPathsExist(self, n: int, edge_list: List[List[int]], queries: List[List[int]]) -> List[bool]:
        uf = UnionFind(n)
        queries_count = len(queries)
        answer = [False] * queries_count;
        
        # Store original indices with all queries.
        queries_with_index = [[] for _ in range(queries_count)]
        for i in range(queries_count):
            queries_with_index[i] = queries[i]
            queries_with_index[i].append(i)
        
        # Sort all edges in increasing order of their edge weights.
        edge_list.sort(key=lambda x: x[2])
        # Sort all queries in increasing order of the limit of edge allowed.
        queries_with_index.sort(key=lambda x: x[2])
        
        edges_index = 0
        
        # Iterate on each query one by one.
        for [p, q, limit, query_original_index] in queries_with_index:
            # We can attach all edges which satisfy the limit given by the query.
            while edges_index < len(edge_list) and edge_list[edges_index][2] < limit:
                node1 = edge_list[edges_index][0]
                node2 = edge_list[edges_index][1]
                uf.join(node1, node2)
                edges_index += 1
            
            # If both nodes belong to the same component, it means we can reach them. 
            answer[query_original_index] = uf.are_connected(p, q)

        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 3
        j = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]]
        k = [[0,1,2],[0,2,5]]
        o = [False, True]
        self.assertEqual(s.distanceLimitedPathsExist(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = 5
        j = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]]
        k = [[0,4,14],[1,4,13]]
        o = [True, False]
        self.assertEqual(s.distanceLimitedPathsExist(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)