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
    Given the root of a full binary tree with the following properties:
    * Leaf nodes have either the value 0 or 1, where 0 represents False and 1
      represents True.
    * Non-leaf nodes have either the value 2 or 3, where 2 represents the
      boolean OR and 3 represents the boolean AND.
    
    The evaluation of a node is as follows:
    * If the node is a leaf node, the evaluation is the value of the node, ie
      True or False.
    * Otherwise, evaluate the node's two children and apply the boolean
      operation of its value with the children's evaluations.
    
    Return the boolean result of evaluating the root node.

    A full binary tree is a binary tree where each node has either 0 or 2
    children.

    A leaf node is a node that has zero children.
    '''
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.val == 0:
            return False
        if root.val == 1:
            return True
        if root.val == 2:
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        if root.val == 3:
            return self.evaluateTree(root.left) and self.evaluateTree(root.right)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(2, TreeNode(1), TreeNode(3, TreeNode(0), TreeNode(1)))
        o = True
        self.assertEqual(s.evaluateTree(i), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(0)
        o = False
        self.assertEqual(s.evaluateTree(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)