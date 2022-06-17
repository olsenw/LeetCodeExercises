# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Optional

from functools import cache

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
    Given the root of a binary tree. It is possible to install cameras
    on the tree nodes where each camera at a node can monitor its
    parent, itself, and its immediate children.

    Return the minimum number of cameras needed to monitor all nodes of
    the tree.
    '''
    # incomplete and overly complicated
    # makes a 2d grid that shows if camera is placed at a node which
    # other nodes would be covered up
    def minCameraCover_unfinished_dynamic(self, root: Optional[TreeNode]) -> int:
        # label graph and return number of nodes O(n)
        def dfs_label(n, p, v = 0):
            if n.left:
                v = dfs_label(n.left, n, v)
            if n.right:
                v = dfs_label(n.right, n, v)
            n.val = v
            return v + 1
        v = dfs_label(root, None)
        # list is left, right, itself, parent
        # g = {i:[] for i in range(v)}
        g = [[0] * v for _ in range(v)]
        def dfs_cam(n, p, g=g):
            # nonlocal g
            if n.left:
                dfs_cam(n.left, n)
                # g[n.val].append(n.left.val)
                g[n.val][n.left.val] = 1
            if n.right:
                dfs_cam(n.right, n)
                # g[n.val].append(n.right.val)
                g[n.val][n.right.val] = 1
            # g[n.val].append(n.val)
            g[n.val][n.val] = 1
            if p:
                # g[n.val].append(p.val)
                g[n.val][p.val] = 1
        dfs_cam(root, None)
        return 0

    '''
    Thought Edmonds' algorithm may have been answer... but not sure.
    Don't think it would selectively pick the intermediate nodes (ie
    cameras) such that there is minimal overlap in outer edges nodes (ie
    the original tree).
    
    https://en.wikipedia.org/wiki/Edmonds%27_algorithm
    '''

    # Leetcode Greedy Solution
    # https://leetcode.com/problems/binary-tree-cameras/solution/
    def minCameraCoverd_Leetcode(self, root: Optional[TreeNode]) -> int:
        cameras = 0
        marked = {None}
        def dfs(n, p=None):
            nonlocal cameras
            if n:
                dfs(n.left, n)
                dfs(n.right, n)
                if p is None and \
                    n not in marked or \
                    n.left not in marked or \
                    n.right not in marked:
                        cameras += 1
                        marked.add(p)
                        marked.add(n)
                        marked.add(n.left)
                        marked.add(n.right)
        dfs(root)
        return cameras

    # variation without using a set
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def dfs(node, parent=None):
            cameras = 0
            # go left
            if node.left:
                cameras += dfs(node.left, node)
            # go right
            if node.right:
                cameras += dfs(node.right, node)
            # Greedy take node
            if (parent is None and not node.val) or \
                (node.left and not node.left.val) or \
                (node.right and not node.right.val):
                if parent:
                    parent.val = 1
                node.val = 1
                cameras += 1
            return cameras
        return dfs(root)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(0, TreeNode(0, TreeNode(0), TreeNode(0)))
        o = 1
        self.assertEqual(s.minCameraCover(i), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(0, TreeNode(0, TreeNode(0, TreeNode(0, None, TreeNode(0)))))
        o = 2
        self.assertEqual(s.minCameraCover(i), o)

    def test_three(self):
        s = Solution()
        i = TreeNode(0, TreeNode(0, TreeNode(0), TreeNode(0, TreeNode(0))))
        o = 2
        self.assertEqual(s.minCameraCover(i), o)

    def test_four(self):
        s = Solution()
        i = TreeNode(0)
        o = 1
        self.assertEqual(s.minCameraCover(i), o)

    def test_five(self):
        s = Solution()
        i = TreeNode(0, TreeNode(0), TreeNode(0, None, TreeNode(0)))
        o = 2
        self.assertEqual(s.minCameraCover(i), o)

    def test_six(self):
        s = Solution()
        i = TreeNode(0, TreeNode(0, None, TreeNode(0, None, TreeNode(0, TreeNode(0, None, TreeNode(0))))))
        o = 2
        self.assertEqual(s.minCameraCover(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)