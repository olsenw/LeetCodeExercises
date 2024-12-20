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
    Given the root of a perfect binary tree, reverse the node value at each odd
    level of the tree.

    Return the root of the reversed tree.

    A binary tree is prefect if all parent nodes have two children and all
    leaves are on the same level.

    The level of a node is the number of edges along the path between it and the
    root node.
    '''
    def reverseOddLevels_fails(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root.left is None:
            return root
        level = 0
        last = []
        curr = [root]
        while curr:
            level += 1
            last = curr
            curr = []
            if last[0] is None:
                break
            for node in last:
                curr.append(node.left)
                curr.append(node.right)
            curr = curr[::-1]
            j = 0
            for i in range(len(last)):
                last[i].left = curr[j]
                last[i].right = curr[j+1]
                j += 2
        return root

    # hints for the win
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(left: Optional[TreeNode], right: Optional[TreeNode], level: int):
            if left is None:
                return
            if level % 2:
                left.val, right.val = right.val, left.val
            dfs(left.left, right.right, level+1)
            dfs(left.right, right.left, level+1)
        dfs(root.left, root.right, 1)
        return root

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(2, TreeNode(3, TreeNode(8), TreeNode(13)), TreeNode(5, TreeNode(21), TreeNode(34)))
        o = TreeNode(2, TreeNode(5, TreeNode(8), TreeNode(13)), TreeNode(3, TreeNode(21), TreeNode(34)))
        self.assertEqual(s.reverseOddLevels(i), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(7, TreeNode(13), TreeNode(11))
        o = TreeNode(7, TreeNode(11), TreeNode(13))
        self.assertEqual(s.reverseOddLevels(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)