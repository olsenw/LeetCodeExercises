# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a directed graph of n nodes numbered from 0 to n - 1, where each node
    has at most one outgoing edge.

    The graph is represented with a given 0-indexed array edges of size of n,
    indicating that there is a directed edge from node i to node edges[i]. If
    there is no outgoing edge from noe i, then edges[i] == -1.f

    Return the length of the longest cycle in the graph. If no cycle exists,
    return -1.

    A cycle is a path that starts and ends at the same node.
    '''
    def longestCycle_tle(self, edges: List[int]) -> int:
        # should only contain nodes that could possibly be part of a cycle
        nodes = set()
        # only keep the nodes with an incoming edge
        for e in edges:
            if e != -1:
                nodes.add(e)
        # remove any nodes that do not have an outgoing edge
        for n in list(nodes):
            if edges[n] == -1:
                nodes.remove(n)
        # hold the longest cycle
        answer = 0
        # preform bfs on each node
        for n in nodes:
            v = set()
            c = n
            l = 0
            while edges[c] != -1:
                if c in v:
                    break
                v.add(c)
                l += 1
                c = edges[c]
            if c == n:
                answer = max(answer, l)
        return answer if answer else -1

    def longestCycle(self, edges: List[int]) -> int:
        answer = 0
        nodes = set(range(len(edges)))
        while nodes:
            curr = nodes.pop()
            visited = {curr:0}
            while edges[curr] in nodes and edges[curr] not in visited:
                visited[edges[curr]] = visited[curr] + 1
                curr = edges[curr]
                nodes.remove(curr)
            if edges[curr] in visited:
                answer = max(answer, visited[curr] + 1 - visited[edges[curr]])
        return answer if answer else -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,3,4,2,3]
        o = 3
        self.assertEqual(s.longestCycle(i), o)

    def test_two(self):
        s = Solution()
        i = [2,-1,3,1]
        o = -1
        self.assertEqual(s.longestCycle(i), o)

    def test_three(self):
        s = Solution()
        i = [4,3,3,4,7,2,3,3]
        o = 3
        self.assertEqual(s.longestCycle(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)