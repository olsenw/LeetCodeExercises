# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    '''
    Given a reference of a node in a connected undirected graph.

    Return a deep copy (clone) of the graph.

    Each node in the graph contains a value (int) and a list
    (List[Node]) of its neighbors.
    '''
    def cloneGraph_Dictionary_Recreate(self, node: Node) -> Node:
        # no nodes to copy... ie empty graph
        if not node:
            return None
        # bfs graph search
        from collections import deque
        # adjacency list
        d = dict()
        # stack for searching
        nodes = deque([node])
        while nodes:
            n = nodes.pop()
            d[n.val] = set()
            for i in n.neighbors:
                d[n.val].add(i.val)
                if i.val not in d:
                    nodes.append(i)
        # turn adjacency list into new nodes
        a = {i: Node(i) for i in d}
        for i in d:
            for j in d[i]:
                a[i].neighbors.append(a[j])
        return a[node.val]

    def cloneGraph_Dictionary_Direct(self, node: Node) -> Node:
        # no nodes to copy... ie empty graph
        if not node:
            return None
        # bfs graph search
        from collections import deque
        # node mapping (node.val to node)
        d = {node.val: Node(node.val)}
        # stack for searching
        nodes = deque([node])
        while nodes:
            n = nodes.pop()
            for i in n.neighbors:
                if i.val not in d:
                    nodes.append(i)
                    d[i.val] = Node(i.val)
                d[n.val].neighbors.append(d[i.val])
        return d[node.val]

class UnitTesting(unittest.TestCase):
    '''
    Testing here is very incomplete... and probably inaccurate.
    Decided to make use of Leetcode example testcase mechanism instead
    of writing my own unit tests for this problem.
    '''

    def test_single_node(self):
        s = Solution()
        i = Node(1)
        o = s.cloneGraph_Dictionary_Recreate(i)
        self.assertEqual(i.val, o.val)
        self.assertEqual(len(i.neighbors), len(o.neighbors))
        self.assertNotEqual(i, o)
        o = s.cloneGraph_Dictionary_Direct(i)
        self.assertEqual(i.val, o.val)
        self.assertEqual(len(i.neighbors), len(o.neighbors))
        self.assertNotEqual(i, o)

    def test_zero_nodes(self):
        s = Solution()
        i = None
        o = s.cloneGraph_Dictionary_Recreate(i)
        self.assertEqual(i, o)
        o = s.cloneGraph_Dictionary_Direct(i)
        self.assertEqual(i, o)

if __name__ == '__main__':
    unittest.main(verbosity=2)