# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    A tree is an undirected graph in which any two vertices are
    connected by exactly one path. (ie connected graph w/o cycles is a
    tree)

    Given a tree with n nodes and an array of n-1 edges where 
    edge[i]=[ai,bi]) indicates an undirected edge between node ai and
    bi in the tree. Any node could be chosen as the root of the tree.

    When node x is selected as the root the tree has a resulting height
    of h. Among all possible rooted trees those with a minimum height
    are called minimum height trees (ie mht).

    The height of a rooted tree is number of edges on the longest 
    downward path between the root and a leaf.

    Return a list of all mht root labels.
    '''
    def findMinHeightTreesNaive(self, n: int, edges: List[List[int]]) -> List[int]:
        # build adjacency list of graph (set of neighbors for node i)
        adjacency = [set() for i in range(n)]
        for l, r in edges: # deconstruct the edge tuples
            adjacency[l].add(r)
            adjacency[r].add(l)
        
        heights = [-1 for i in range(n)]

        for root in range(n):
            # iterative DFS based on wikipedia pseudocode
            stack = []
            visited = [-1 for i in range(n)]
            stack.append((root, 0)) # tuple(node, depth)
            while stack: # while stack is not empty
                v, d = stack.pop()
                if visited[v] < 0:
                    visited[v] = d
                    for edges in adjacency[v]:
                        stack.append((edges, d + 1))
            heights[root] = max(visited)
        return [i for i in range(n) if heights[i] == min(heights)]

    '''
    based on topological/centroid solution given by leetcode...
    my naive solution times out
    '''
    def findMinHeightTreesCentroids(self, n: int, edges: List[List[int]]) -> List[int]:
        # base case where answer is known (ie trivial cases)
        if n <= 2:
            return [i for i in range(n)]
        
        # build adjacency list of graph (set of neighbors for node i)
        adjacency = [set() for i in range(n)]
        for l, r in edges: # deconstruct the edge tuples
            adjacency[l].add(r)
            adjacency[r].add(l)
        
        # find all the leaf nodes (python list comprehension)
        leaves = [i for i in range(n) if len(adjacency[i]) == 1]

        # iteratively trim leaves (until base case occurs, 1 or 2 centroids)
        while n > 2:
            new_leaves = []
            n -= len(leaves)
            # remove leaf node edges from adjacency list
            for l in leaves:
                d = adjacency[l].pop() # remove leafs only edge node
                adjacency[d].remove(l) # remove leaf from neighbor's edges
                if len(adjacency[d]) == 1: # neighbor is leaf node
                    new_leaves.append(d) # mark it for removal
            # update the list of leaves for next iteration
            leaves = new_leaves

        # these leaves are the 1 or 2 centroids in middle aka mht roots
        return leaves

class UnitTesting(unittest.TestCase):
    # actual test to run on Solution
    def test_one(self):
        s = Solution()
        n = 4
        e = [[1,0],[1,2],[1,3]]
        o = [1]
        self.assertEqual(s.findMinHeightTreesNaive(n, e), o)
        self.assertEqual(s.findMinHeightTreesCentroids(n, e), o)

    def test_two(self):
        s = Solution()
        n = 6
        e = [[3,0],[3,1],[3,2],[3,4],[5,4]]
        o = [3,4]
        self.assertEqual(s.findMinHeightTreesNaive(n, e), o)
        self.assertEqual(s.findMinHeightTreesCentroids(n, e), o)

    def test_three(self):
        s = Solution()
        n = 1
        e = []
        o = [0]
        self.assertEqual(s.findMinHeightTreesNaive(n, e), o)
        self.assertEqual(s.findMinHeightTreesCentroids(n, e), o)

    def test_four(self):
        s = Solution()
        n = 2
        e = [[0,1]]
        o = [0,1]
        self.assertEqual(s.findMinHeightTreesNaive(n, e), o)
        self.assertEqual(s.findMinHeightTreesCentroids(n, e), o)

    def test_five(self):
        s = Solution()
        n = 6
        e = [[0,1],[0,2],[0,3],[3,4],[4,5]]
        o = [3]
        self.assertEqual(s.findMinHeightTreesNaive(n, e), o)
        self.assertEqual(s.findMinHeightTreesCentroids(n, e), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)