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
    def __eq__(self, value):
        return self.val == value.val and self.left == value.left and self.right == value.right

class Solution:
    '''
    Given two integer arrays, preorder and postorder where preorder is the
    preorder traversal of a binary tree of distinct values and postorder is the
    postorder traversal of the same tree, reconstruct and return the binary
    tree.

    If there exist multiple answers, return any of them.
    '''
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        answer = TreeNode(preorder[0])
        if len(preorder) == 1:
            return answer
        left = postorder.index(preorder[1])
        answer.left = self.constructFromPrePost(preorder[1:left+2], postorder[:left+1])
        answer.right = self.constructFromPrePost(preorder[left+2:], postorder[left+1:len(postorder)-1])
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,4,5,3,6,7]
        j = [4,5,2,6,7,3,1]
        o = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
        self.assertEqual(s.constructFromPrePost(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1]
        j = [1]
        o = TreeNode(1)
        self.assertEqual(s.constructFromPrePost(i,j), o)

    def test_three(self):
        s = Solution()
        i = [1,2,3,4,5,6]
        j = [5,4,6,3,2,1]
        o = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(5)), TreeNode(6))))
        self.assertEqual(s.constructFromPrePost(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)