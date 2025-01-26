# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict, deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A company is organizing a meeting and has a list of n employees, waiting to
    be invited. They have arranged for a large circular table, capable of
    seating any number of employees.

    The employees are numbered from 0 to n - 1. Each employee has a favorite
    person and they will attend the meeting only if they can sit next to their
    favorite person at the table. The favorite person of an employee is not
    themself.

    Given a 0-indexed integer array of favorites, where favorites[i] denotes the
    favorite person of the ith employee, return the maximum number of employees
    that can be invited to the meeting.
    '''
    # based on Leetcode solutions
    # answer is the longest cycle
    # or sum of chains that have a mutual pairs
    # https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/editorial/?envType=daily-question&envId=2025-01-26
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        # reversed graph (each node points to people who favorite node)
        graph = defaultdict(list)
        for i,j in enumerate(favorite):
            graph[j].append(i)
        def bfs(node:int, visited:set[int]) -> int:
            queue = deque([(node,0)])
            maxDistance = 0
            while queue:
                node, distance = queue.popleft()
                for i in graph[node]:
                    if i in visited:
                        continue
                    visited.add(i)
                    queue.append((i, distance + 1))
                    maxDistance = max(maxDistance, distance + 1)
            return maxDistance
        visited = [False] * n
        longestCycle = 0
        # cycles of length two (ie nodes point to each other)
        mutualCycle = 0
        for i in range(n):
            if visited[i]:
                continue
            v = dict()
            c = i
            d = 0
            while True:
                if visited[c]:
                    break
                visited[c] = True
                v[c] = d
                d += 1
                p = favorite[c]
                # cycle detected
                if p in v:
                    cycle = d - v[p]
                    longestCycle = max(longestCycle, cycle)
                    # deal with length two cycles
                    if cycle == 2:
                        nodes = {c, p}
                        mutualCycle += 2 + bfs(p, nodes) + bfs(c, nodes)
                    break
                c = p
        return max(longestCycle, mutualCycle)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,2,1,2]
        o = 3
        self.assertEqual(s.maximumInvitations(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,0]
        o = 3
        self.assertEqual(s.maximumInvitations(i), o)

    def test_three(self):
        s = Solution()
        i = [3,0,1,4,1]
        o = 4
        self.assertEqual(s.maximumInvitations(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)