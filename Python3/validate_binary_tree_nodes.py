# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given n binary tree nodes numbered from 0 to n - 1 where node i has two
    children leftChild[i] rightChild[i], return true if and only if all the
    given nodes nodes form exactly one valid binary tree.

    If node i has no left children then leftChild[i] will equal -1, similarly
    for the right child.

    Note that the nodes have no values and that only the nodes numbers are used
    in this problem.
    '''
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        graph = {i:set() for i in range(n)}
        for i,j in enumerate(leftChild):
            if j > -1:
                graph[j].add(i)
        for i,j in enumerate(rightChild):
            if j > -1:
                graph[j].add(i)
        a,b,c = 0,0,0
        for i in range(n):
            if len(graph[i]) == 0:
                a += 1
                c = i
            elif len(graph[i]) == 1:
                b += 1
        if a != 1 or b != n - 1:
            return False
        def dfs(i):
            a,b = 0,0
            if leftChild[i] != -1:
                a = dfs(leftChild[i])
            if rightChild[i] != -1:
                b = dfs(rightChild[i])
            return a + b + 1
        return dfs(c) == n

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 4
        j = [1,-1,3,-1]
        k = [2,-1,-1,-1]
        o = True
        self.assertEqual(s.validateBinaryTreeNodes(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = 4
        j = [1,-1,3,-1]
        k = [2,3,-1,-1]
        o = False
        self.assertEqual(s.validateBinaryTreeNodes(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = 2
        j = [1,0]
        k = [-1,-1]
        o = False
        self.assertEqual(s.validateBinaryTreeNodes(i,j,k), o)

    def test_four(self):
        s = Solution()
        i = 2
        j = [-1,0]
        k = [-1,-1]
        o = True
        self.assertEqual(s.validateBinaryTreeNodes(i,j,k), o)

    def test_five(self):
        s = Solution()
        i = 4
        j = [1,0,3,-1]
        k = [-1,-1,-1,-1]
        o = False
        self.assertEqual(s.validateBinaryTreeNodes(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)