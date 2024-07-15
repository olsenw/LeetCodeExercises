# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
    Given a 2D integer array descriptions where
    descriptions[i] = [parenti, childi, isLefti] indicates that parenti is the
    parent of childi in a binary tree of unique values. Furthermore:
    * if isLefti == 1, then childi is the left child of parenti.
    * if isLefti == 0, then childj is the right child or parenti.

    Construct the binary tree described by descriptions and return its root.

    The test cases will be generated such that the binary tree is valid.
    '''
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = dict()
        parents = dict()
        for a,b,c in descriptions:
            if b not in nodes:
                parents[b] = None
                nodes[b] = TreeNode(b)
            if a not in nodes:
                parents[a] = None
                if c == 0:
                    nodes[a] = TreeNode(a, None, nodes[b])
                else:
                    nodes[a] = TreeNode(a, nodes[b])
            else:
                if c == 0:
                    nodes[a].right = nodes[b]
                else:
                    nodes[a].left = nodes[b]
            parents[b] = nodes[a]
        for p in parents:
            if parents[p] == None:
                return nodes[p]
        return None

class UnitTesting(unittest.TestCase):
    '''
    Tested online because lazy
    '''
    pass
    # def test_one(self):
    #     s = Solution()
    #     i = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
    #     o = [50,20,80,15,17,19]
    #     self.assertEqual(s.createBinaryTree(i), o)

    # def test_two(self):
    #     s = Solution()
    #     i = [[1,2,1],[2,3,0],[3,4,1]]
    #     o = [1,2,None,None,3,4]
    #     self.assertEqual(s.createBinaryTree(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)