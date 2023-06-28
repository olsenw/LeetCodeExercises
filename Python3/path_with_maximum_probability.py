# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import math
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an undirected weighted graph of n nodes (0-indexed), represented by an
    edge list where edges[i] = [a,b] is an undirected edge connecting the nodes
    a and b with a probability of success of traversing that edge succProb[i].

    Given two nodes start and end, find the path with the maximum probability of
    success to go from start to end and return its success probability.

    If there is no path from start to end, return 0. Answers will be excepted if
    there is less than 1e-5 difference from the correct answer.
    '''
    # hints important (log(ab) = log(a) + log(b))
    # https://simple.wikipedia.org/wiki/Dijkstra%27s_algorithm
    # time limit exceeded (13/18)
    def maxProbability_tle(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        succProb = [-math.log(i) for i in succProb]
        
        graph = {i:set() for i in range(n)}
        for i,(j,k) in enumerate(edges):
            graph[j].add((k, i))
            graph[k].add((j, i))
        
        vertices = set(range(n))
        distance = {i:math.inf for i in range(n)}
        distance[start] = 0.0
        while vertices:
            i = min(vertices,key=lambda x: distance[x])
            vertices.remove(i)
            if i == end:
                return math.exp(-distance[end])
            for j,k in graph[i]:
                if j in vertices:
                    dist = distance[i] + succProb[k]
                    if dist < distance[j]:
                        distance[j] = dist
        return 0.0
    
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        succProb = [-math.log(i) for i in succProb]
        
        graph = {i:set() for i in range(n)}
        for i,(j,k) in enumerate(edges):
            graph[j].add((k, i))
            graph[k].add((j, i))
        
        vertices = set()
        heap = [(0,start)]
        while heap:
            d,i = heapq.heappop(heap)
            vertices.add(i)
            if i == end:
                return math.exp(-d)
            for j,k in graph[i]:
                if j not in vertices:
                    heapq.heappush(heap, (d + succProb[k], j))
        return 0.0

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 3
        j = [[0,1],[1,2],[0,2]]
        k = [0.5,0.5,0.2]
        l = 0
        m = 2
        o = 0.25
        self.assertEqual(s.maxProbability(i,j,k,l,m), o)

    def test_two(self):
        s = Solution()
        i = 3
        j = [[0,1],[1,2],[0,2]]
        k = [0.5,0.5,0.3]
        l = 0
        m = 2
        o = 0.3
        self.assertEqual(s.maxProbability(i,j,k,l,m), o)

    def test_three(self):
        s = Solution()
        i = 3
        j = [[0,1]]
        k = [0.5]
        l = 0
        m = 2
        o = 0.0
        self.assertEqual(s.maxProbability(i,j,k,l,m), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)