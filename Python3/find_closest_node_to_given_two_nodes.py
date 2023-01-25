# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a directed graph of n nodes numbered from 0 to n - 1, where each node
    has at most one outgoing edge.

    The graph is represented with a given 0-indexed array edges of size n,
    indicating that there is a directed edge from node i to node edges[i]. If
    there is no outgoing edges from i, then edges[i] == -1.

    Given the indexes of two nodes, node1 and node2, return the index of the
    node that can be reached from both nodes such that the maximum distance from
    node1 to node2 is minimized. If there are multiple answers, return the node
    with the smallest index, and if no possible answer exists return -1.

    Note that edges may contain cycles.
    '''
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        a = [-1] * len(edges)
        a[node1] = 0
        node = node1
        while edges[node] != -1 and a[edges[node]] == -1:
            a[edges[node]] = a[node] + 1
            node = edges[node]
        b = [-1] * len(edges)
        b[node2] = 0
        node = node2
        while edges[node] != -1 and b[edges[node]] == -1:
            b[edges[node]] = b[node] + 1
            node = edges[node]
        ans = min((max(j[0], j[1]), i) if j[0] > -1 and j[1] > -1 else (10**5, i) for i,j in enumerate(zip(a,b)))
        return ans[1] if ans[0] < 10**5 else -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,2,3,-1]
        j = 0
        k = 1
        o = 2
        self.assertEqual(s.closestMeetingNode(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = [1,2,-1]
        j = 0
        k = 2
        o = 2
        self.assertEqual(s.closestMeetingNode(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = [1,2,0]
        j = 0
        k = 2
        o = 0
        self.assertEqual(s.closestMeetingNode(i,j,k), o)

    def test_four(self):
        s = Solution()
        i = [1,-1,-1]
        j = 0
        k = 2
        o = -1
        self.assertEqual(s.closestMeetingNode(i,j,k), o)

    def test_five(self):
        s = Solution()
        i = [4,4,8,-1,9,8,4,4,1,1]
        j = 5
        k = 6
        o = 1
        self.assertEqual(s.closestMeetingNode(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)