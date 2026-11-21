# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a tree rooted at nodes 0 that consists of n nodes numbered from 0 to
    n - 1. The tree is represented by an array parent of size nm where parent[i]
    is the parent of node i. since the node 0 is the root, parent[0] == -1.

    Also given a string s of length n, where s[i] is the character assigned to 
    node i.

    The following changes are made to the tree simultaneously for all nodes x
    from 1 to n - 1.
    * Find the closest node y to node x such that y is an ancestor of x, and
      s[x] == s[y].
    * If node y does not exist, do nothing.
    * Otherwise remove the edge between x and its current parent and make y the
      new parent of x by adding an edge between them.
    
    Return an array answer of size n where answer[i] is the size of the subtree
    rooted at node i in the final tree.
    '''
    def findSubtreeSizes_tle(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        reparent = list(parent)
        for i in range(n):
            j = parent[i]
            while j > -1 and s[i] != s[j]:
                j = parent[j]
            if j == -1:
                continue
            reparent[i] = j
        graph = {i:[] for i in range(n)}
        for i in range(1, n):
            graph[reparent[i]].append(i)
        answer = [0] * n
        def child(node:int) -> int:
            children = 1
            for c in graph[node]:
                children += child(c)
            answer[node] = children
            return children
        child(0)
        return answer

    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        graph = {i:[] for i in range(n)}
        for i in range(1,n):
            graph[parent[i]].append(i)
        # letter -> [(node, depth)]
        seen = {i:[] for i in "abcdefghijklmnopqrstuvwxyz"}
        def reparent(node:int, depth:int) -> None:
            # while seen[s[node]] and seen[s[node]][-1][1] >= depth:
                # seen[s[node]].pop()
            if seen[s[node]]:
                # parent[node] = seen[s[node]][-1][0]
                parent[node] = seen[s[node]][-1]
            # seen[s[node]].append((node, depth))
            seen[s[node]].append(node)
            for i in graph[node]:
                reparent(i, depth+1)
            seen[s[node]].pop()
        reparent(0,0)
        graph = {i:[] for i in range(n)}
        for i in range(1, n):
            graph[parent[i]].append(i)
        answer = [0] * n
        def child(node:int) -> int:
            children = 1
            for c in graph[node]:
                children += child(c)
            answer[node] = children
            return children
        child(0)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [-1,0,0,1,1,1]
        j = "abaabc"
        o = [6,3,1,1,1,1]
        self.assertEqual(s.findSubtreeSizes(i,j), o)

    def test_two(self):
        s = Solution()
        i = [-1,0,4,0,1]
        j = "abbba"
        o = [5,2,1,1,1]
        self.assertEqual(s.findSubtreeSizes(i,j), o)

    def test_four(self):
        s = Solution()
        i = [-1,10,0,12,10,18,11,12,2,3,2,2,2,0,4,11,4,2,0]
        j = "babadabbdabcbaceeda"
        o = [19,1,15,2,3,1,1,1,1,1,5,2,4,1,1,1,1,1,2]
        self.assertEqual(s.findSubtreeSizes(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)