# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There are n computers numbered from 0 to n - 1 connected by ethernet cables
    connections forming a network where connections[i] = [ai, bi] represents a
    connection between computers ai and bi. Any computer can reach any other
    computer directly or indirectly through the network.

    Given an initial computer network connections. It is possible to extract
    certain cables two directly connected computers, and place the cables
    between any pair of disconnected computers to make them directly connected.

    Return the minimum number of times the above procedure needs to be done in
    order to make all the computers connected. If it is not possible, return -1.
    '''
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        graph = {i:[] for i in range(n)}
        for i,j in connections:
            graph[i].append(j)
            graph[j].append(i)
        answer = 0
        nodes = {i for i in range(n)}
        while nodes:
            q = deque([nodes.pop()])
            nodes.add(q[0])
            while q:
                curr = q.popleft()
                if curr not in nodes:
                    continue
                nodes.remove(curr)
                for i in graph[curr]:
                    q.append(i)
            answer += 1
        return answer - 1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 4
        j = [[0,1],[0,2],[1,2]]
        o = 1
        self.assertEqual(s.makeConnected(i,j), o)

    def test_two(self):
        s = Solution()
        i = 6
        j = [[0,1],[0,2],[0,3],[1,2],[1,3]]
        o = 2
        self.assertEqual(s.makeConnected(i,j), o)

    def test_three(self):
        s = Solution()
        i = 6
        j = [[0,1],[0,2],[0,3],[1,2]]
        o = -1
        self.assertEqual(s.makeConnected(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)