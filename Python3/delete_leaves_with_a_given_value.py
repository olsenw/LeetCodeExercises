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
    Given a binary tree root and an integer target, delete all the leaf nodes
    with value target.

    Note that once a leaf node with value target, if the parent node becomes a
    leaf node and has the value target, it should also be deleted (repeat until
    it is no longer possible).
    '''
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(node, parent, left):
            if node.left:
                dfs(node.left, node, True)
            if node.right:
                dfs(node.right, node, False)
            if node.val == target and not node.left and not node.right:
                if left:
                    parent.left = None
                else:
                    parent.right = None
            return
        t = TreeNode(0, root)
        dfs(root, t, True)
        return t.left

class UnitTesting(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main(verbosity=2)