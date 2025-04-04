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
    Given the root of a binary tree, return the lowest common ancestor of its
    deepest leaves.

    Recall that:
    * The node of a binary tree is a leaf if and only if it has no children
    * The depth of the root of the tree is 0. If the depth of a node is d, the
      depth of each of its children is d + 1.
    * The lowest common ancestor of a set S of nodes is the node A with the
      largest depth such that every node in S in the subtree with root A.
    '''
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        maxDepth = 0
        answer = None
        def dfs(node: TreeNode, depth: int):
            nonlocal maxDepth
            nonlocal answer
            if node.left and node.right:
                l = dfs(node.left, depth+1)
                r = dfs(node.right, depth+1)
                if l == r and l == maxDepth:
                    answer = node
                return max(l,r)
            elif node.left:
                return dfs(node.left, depth+1)
            elif node.right:
                return dfs(node.right, depth+1)
            else:
                if depth > maxDepth:
                    maxDepth = depth
                    answer = node
                return depth
        dfs(root,1)
        return answer

class UnitTesting(unittest.TestCase):
    # tested online
    pass

if __name__ == '__main__':
    unittest.main(verbosity=2)