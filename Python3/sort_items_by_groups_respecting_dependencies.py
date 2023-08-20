# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There are n items each belonging to zero or one of m groups where group[i]
    is the group that the ith item belongs to and its equal to -1 if the ith
    item belongs to no group. The items and the groups are zero indexed. a group
    can have no item belonging to it.

    Return a sorted list of the items such that:
    * The items that belong to the same group are next to each other in the
      sorted list.
    * There are some relations between these items where beforeItems[i] is a
      list containing all the items that should come before the ith item in the
      sorted array (to the left of the ith item).
    
    Return any solution if there is more than one solution and return an empty
    list if there is no solution.
    '''
    # based on editorial 
    # https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/editorial/
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        # assign ungrouped items to own groups
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1
        
        # sort items without group dependencies
        itemGraph = [[] for _ in range(n)]
        itemIndegree = [0] * n
        
        # sort groups without item dependencies
        groupGraph = [[] for _ in range(m)]
        groupIndgree = [0] * m
        
        for i in range(n):
            for j in beforeItems[i]:
                # j -> i represents dependency in itemGraph
                itemGraph[j].append(i)
                itemIndegree[i] += 1
                # add group dependence
                if group[i] != group[j]:
                    groupGraph[group[j]].append(group[i])
                    groupIndgree[group[i]] += 1
        
        # perform topological sort (returns [] if cycle detected)
        def topologicalSort(graph, indegree):
            visited = []
            stack = [i for i in range(len(graph)) if indegree[i] == 0]
            while stack:
                cur = stack.pop()
                visited.append(cur)
                for neighbor in graph[cur]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        stack.append(neighbor)
            return visited if len(visited) == len(graph) else []
        
        itemOrder = topologicalSort(itemGraph, itemIndegree)
        groupOrder = topologicalSort(groupGraph, groupIndgree)

        if not itemOrder or not groupOrder:
            return []
        
        # correct item order to account group order
        orderedGroups = defaultdict(list)
        for i in itemOrder:
            orderedGroups[group[i]].append(i)
        
        # generate answer from sorted groups
        answer = []
        for g in groupOrder:
            answer += orderedGroups[g]
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 8
        j = 2
        k = [-1,-1,1,0,0,1,0,-1]
        l = [[],[6],[5],[6],[3,6],[],[],[]]
        o = [6,3,4,1,5,2,0,7]
        self.assertEqual(s.sortItems(i,j,k,l), o)

    def test_two(self):
        s = Solution()
        i = 8
        j = 2
        k = [-1,-1,1,0,0,1,0,-1]
        l = [[],[6],[5],[6],[3],[],[4],[]]
        o = []
        self.assertEqual(s.sortItems(i,j,k,l), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)