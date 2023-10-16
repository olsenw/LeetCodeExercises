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
    Given the roots of two binary trees root and subRoot, return true if there
    is a subtree of root with the same structure and nodes values of subRoot and
    false otherwise.

    A subtree of a binary tree tree is a tree that consists of a node in tree
    and all of this node's descendants. The tree tree could also be considered a
    subtree of itself.
    '''
    # does not descend the tree correctly (can skips nodes when matching)
    def isSubtree_wrong(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        m = False
        if root.val == subRoot.val:
            m = self.isSubtree(root.left, subRoot.left) and self.isSubtree(root.right, subRoot.right)
        return m or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(i: Optional[TreeNode], j: Optional[TreeNode]):
            if not i and not j:
                return True
            if not i or not j or i.val != j.val:
                return False
            return dfs(i.left, j.left) and dfs(i.right, j.right)
        if not root or not subRoot:
            return False
        return dfs(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

class UnitTesting(unittest.TestCase):
    # tested online
    pass

if __name__ == '__main__':
    unittest.main(verbosity=2)