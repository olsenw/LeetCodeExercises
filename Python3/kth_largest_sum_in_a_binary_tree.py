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
    Given the root of a binary tree and a positive integer k.

    The level sum in the tree is the sum of the values of the nodes that are on
    the same level.

    Return the kth largest level sum in the tree (not necessarily distinct). If
    there are fewer than k levels in the tree, return -1.

    Note that two nodes are on the same level if they have the same distance
    from the root.
    '''
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        sums = []
        def dfs(node: TreeNode, depth: int):
            if len(sums) < depth:
                sums.append(0)
            sums[depth-1] += node.val
            if node.left:
                dfs(node.left, depth+1)
            if node.right:
                dfs(node.right, depth+1)
        dfs(root, 1)
        return -1 if len(sums) < k else sorted(sums, reverse=True)[k-1]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(5, TreeNode(8, TreeNode(2, TreeNode(4), TreeNode(6)), TreeNode(1)), TreeNode(9, TreeNode(3), TreeNode(7)))
        o = 13
        self.assertEqual(s.kthLargestLevelSum(i,2), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(1, TreeNode(2, TreeNode(3)))
        o = 3
        self.assertEqual(s.kthLargestLevelSum(i,1), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)