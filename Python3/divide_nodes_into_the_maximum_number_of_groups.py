# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a positive integer n representing the number of nodes in an undirected
    graph. The nodes are labeled from 1 to n.

    Also given a 2D integer array edges, where edges[i] = [ai, bi] indicates
    that there is a bidirectional edge between nodes ai and bi. Notice that the
    given graph may be disconnected.

    Divide the nodes of the graph into m groups (1-indexed) such that:
    * Each node in the graph belongs into exactly one group.
    * For every pair of nodes in the graph that are connected by an edge
      [ai, bi], if ai belongs to the group with index x, and bi belongs to the
      group with index y, then abs(y-x) == 1.

    Return the maximum number of groups (i.e. maximum m) into which the nodes
    can be divided. Return -1 if it is impossible to group the nodes with the
    current conditions
    '''
    # based on leetcode editorial
    # https://leetcode.com/problems/divide-nodes-into-the-maximum-number-of-groups/editorial/?envType=daily-question&envId=2025-01-30
    # check if graph is bipartite (ie possible to split into two groups)
    # calculate the width of each component starting at given node
    # sum up the maximum width for all components
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        graph = {i:[] for i in range(n)}
        for i,j in edges:
            graph[i-1].append(j-1)
            graph[j-1].append(i-1)
        colors = [-1] * n
        def isBipartite(node:int) -> bool:
            for neighbor in graph[node]:
                # if two nodes have same color and are neighbors, cannot be bipartite
                if colors[neighbor] == colors[node]:
                    return False
                # check if already examined
                if colors[neighbor] != -1:
                    continue
                # assign color to neighbor
                if colors[node] == 0:
                    colors[neighbor] = 1
                else:
                    colors[neighbor] = 0
                # recursively check if bipartite
                if isBipartite(neighbor) == False:
                    return False
            return True
        # check if graph is bipartite
        for node in range(n):
            if colors[node] != -1:
                continue
            # paint initial node of component
            colors[node] = 0
            if isBipartite(node) == False:
                return -1
        def path(node:int)->int:
            # bfs
            queue = deque([node])
            visited = [False] * n
            visited[node] = True
            distance = 0
            while queue:
                # process current layer
                for _ in range(len(queue)):
                    curr = queue.popleft()
                    for neighbor in graph[curr]:
                        if visited[neighbor]:
                            continue
                        visited[neighbor] = True
                        queue.append(neighbor)
                # increment the distance of the next layer
                distance += 1
            return distance
        # calculate the distance for each node
        distances = [path(node) for node in range(n)]
        def components(node):
            groups = distances[node]
            visited[node] = True
            # get answer for unvisited nodes
            for neighbor in graph[node]:
                if visited[neighbor]:
                    continue
                groups = max(groups, components(neighbor))
            return groups
        # calculate max number of groups over components
        answer = 0
        visited = [False] * n
        for node in range(n):
            if visited[node]:
                continue
            # add answer of connected component
            answer += components(node)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 6
        j = [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]
        o = 4
        self.assertEqual(s.magnificentSets(i,j), o)

    def test_two(self):
        s = Solution()
        i = 3
        j = [[1,2],[2,3],[3,1]]
        o = -1
        self.assertEqual(s.magnificentSets(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)