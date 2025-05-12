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
    Given two binary trees root1 and root2.

    Merge the two trees into a new binary tree. The merge rule is that if two
    nodes overlap, then sum node value up as the new value of the merged node.
    Otherwise, the none null node will be used as the node of the new tree.

    Return the merged tree.

    Note: The merging process must start from the root nodes of both trees.
    '''
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            return None
        answer = TreeNode(0)
        if root1:
            answer.val += root1.val
        if root2:
            answer.val += root2.val
        answer.left = self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
        answer.right = self.mergeTrees(root1.right if root1 else None, root2.right if root2 else None)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2))
        j = TreeNode(2, TreeNode(1, None, TreeNode(4)), TreeNode(3, None, TreeNode(7)))
        o = TreeNode(3, TreeNode(4, TreeNode(5), TreeNode(4)), TreeNode(5, None, TreeNode(7)))
        self.assertEqual(s.mergeTrees(i,j), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(1)
        j = TreeNode(1, TreeNode(2))
        o = TreeNode(2, TreeNode(2))
        self.assertEqual(s.mergeTrees(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)