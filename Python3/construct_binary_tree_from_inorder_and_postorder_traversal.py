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
    Given two integer arrays inorder and postorder where inorder is the inorder
    traversal of a binary tree and postorder is the postorder traversal of the
    same tree, construct and return the binary tree.
    '''
    # too lazy to figure out the recursion
    # solution based on discussion post by archit91
    # https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/solutions/1589310/c-python-2-simple-solutions-w-images-and-detailed-explanation-recursion-hashmap/
    # inorder is left -> root -> right
    # postorder is left -> right -> root
    # build root then right subtree then left subtree
    # postorder will give root of each subtree
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        index = len(postorder) - 1
        def build(i,j):
            if i > j:
                return None
            nonlocal index
            root = TreeNode(postorder[index])
            index -= 1
            # need to use index because array is unsorted, preventing binary search
            root.right = build(inorder.index(root.val, i, j+1) + 1, j)
            root.left = build(i, inorder.index(root.val, i, j+1) - 1)
            return root
        return build(0, len(inorder) - 1)

class UnitTesting(unittest.TestCase):
    '''
    Test online because reused code
    '''
    pass

if __name__ == '__main__':
    unittest.main(verbosity=2)