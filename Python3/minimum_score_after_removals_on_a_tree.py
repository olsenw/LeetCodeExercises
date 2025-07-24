# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache, reduce
from operator import xor
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There is an undirected connected tree with n nodes labeled from 0 to n - 1
    and n - 1 edges.

    Given a 0-index integer array nums of length n where nums[i] represents the
    value of the ith node. Also given a 2D integer array edges of length n - 1
    where edge[i] = [ai, bi] indicates that there is an edge between nodes ai
    and bi in the tree.

    Remove two distinct edges of the tree to form three connected components.
    For a pair of removed edges, the following steps are defined:
    1. Get the XOR of all the values of the nodes for each of the three
       components respectively.
    2. The difference between the largest XOR value and smallest XOR value is
       score of the pair.
    
    Return the minimum score of any possible pair of edge removals on the given
    tree.
    '''
    # does not separate component correctly (xor math will double count)
    def minimumScore_fails(self, nums: List[int], edges: List[List[int]]) -> int:
        graph = {i:set() for i in range(len(nums))}
        parent = [-1] * len(nums)
        for i,j in edges:
            graph[i].add(j)
            graph[j].add(i)
        @cache
        def dfs(node:int, last:int) -> int:
            parent[node] = last
            answer = [nums[node]]
            for i in graph[node]:
                if i == last:
                    continue
                answer.append(dfs(i, node))
            return reduce(xor, answer)
        root = dfs(0,-1)
        answer = float('inf')
        '''
        This part fails
        Does not account for one edge begin contained in the component of
        another edge
        '''
        for i in range(len(edges)):
            a,b = edges[i]
            if parent[a] == b:
                a,b = b,a
            for j in range(i+1, len(edges)):
                x,y = edges[j]
                if parent[x] == y:
                    x,y = y,x
                s,_,t = sorted([root ^ dfs(b,a) ^ dfs(y,x), dfs(b,a), dfs(y,x)])
                answer = min(answer, t - s)
        return answer

    # after reading hints
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        answer = float('inf')
        parent: List[int]
        calcs: List[int]
        comp: List[int]
        graph = {i:set() for i in range(len(nums))}
        for i,j in edges:
            graph[i].add(j)
            graph[j].add(i)
        def dfs(node:int, last:int, component:int) -> int:
            parent[node] = last
            comp[node] = component
            answer = nums[node]
            for i in graph[node]:
                if i != last:
                    answer ^= dfs(i, node, component)
            calcs[node] = answer
            return answer
        # iterate over all edges for first removed edge
        for i in range(len(edges)):
            parent = [-1] * len(nums)
            calcs = [-1] * len(nums)
            comp = [-1] * len(nums)
            a,b = edges[i]
            # remove an edge and break graph into two parts
            graph[a].remove(b)
            graph[b].remove(a)
            dfs(a, -1, 1)
            dfs(b, -1, 2) 
            # iterate over all remaining edges for second removed edge
            for j in range(i + 1, len(edges)):
                x,y = edges[j]
                if parent[y] == x:
                    x,y = y,x
                if comp[x] == 1:
                    s,_,t = sorted([calcs[a] ^ calcs[x], calcs[x], calcs[b]])
                    answer = min(answer, t - s)
                else:
                    s,_,t = sorted([calcs[a], calcs[b] ^ calcs[x], calcs[x]])
                    answer = min(answer, t - s)
            # add edge to restore components
            graph[a].add(b)
            graph[b].add(a)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,5,5,4,11]
        j = [[0,1],[1,2],[1,3],[3,4]]
        o = 9
        self.assertEqual(s.minimumScore(i,j), o)

    def test_two(self):
        s = Solution()
        i = [5,5,2,4,4,2]
        j = [[0,1],[1,2],[5,2],[4,3],[1,3]]
        o = 0
        self.assertEqual(s.minimumScore(i,j), o)

    def test_three(self):
        s = Solution()
        i = [1,2,3]
        j = [[0,1],[1,2]]
        o = 2
        self.assertEqual(s.minimumScore(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)