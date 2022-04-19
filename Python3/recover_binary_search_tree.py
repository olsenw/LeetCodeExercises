# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __eq__(self, other):
        return type(other) == TreeNode and self.val == other.val and \
            self.left == other.left and self.right == other.right

class Solution:
    '''
    Given the root of a binary search tree (BST), where the values of
    exactly two nodes of the tree were swapped by mistake. Recover the
    tree without changing its structure.
    '''
    # O(n) time
    # O(n) space
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        a = []
        def r(root):
            if root.left:
                r(root.left)
            a.append(root)
            if root.right:
                r(root.right)
        r(root)
        b = [i.val for i in a]
        i = 0
        while i < len(a) - 2:
            if a[i].val > a[i+1].val:
                break
            i += 1
        j = len(a) - 1
        while j > 0:
            if a[j].val < a[j-1].val:
                break
            j -= 1
        a[i].val, a[j].val = a[j].val, a[i].val
        c = [i.val for i in a]
        pass

    '''
    To do follow up do constant space dfs search, and when find mismatch
    swap the nodes and continue on with the search.
    '''

    # 850/1919 test cases does not handle swap across tree (ie same level)
    def recoverTree_fails(self, root: Optional[TreeNode]) -> None:
        def l(root, node):
            if root.val > node.val:
                node.val, root.val = root.val, node.val
                raise Exception('left')
            if root.left:
                l(root.left, node)
            if root.right:
                l(root.right, node)
            recurse(root)
        def r(root, node):
            if root.val < node.val:
                node.val, root.val = root.val, node.val
                raise Exception('right')
            if root.left:
                r(root.left, node)
            if root.right:
                r(root.right, node)
            recurse(root)
        def recurse(root):
            if root.left:
                l(root.left, root)
            if root.right:
                r(root.right, root)
        try:
            recurse(root)
        except:
            return

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(1, TreeNode(3, None, TreeNode(2)))
        o = TreeNode(3, TreeNode(1, None, TreeNode(2)))
        s.recoverTree(i)
        self.assertEqual(i, o)

    def test_two(self):
        s = Solution()
        i = TreeNode(3, TreeNode(1), TreeNode(4, TreeNode(2)))
        o = TreeNode(2, TreeNode(1), TreeNode(4, TreeNode(3)))
        s.recoverTree(i)
        self.assertEqual(i, o)

    def test_three(self):
        s = Solution()
        i = TreeNode(0, TreeNode(1))
        o = TreeNode(1, TreeNode(0))
        s.recoverTree(i)
        self.assertEqual(i, o)

    def test_four(self):
        s = Solution()
        i = TreeNode(2, TreeNode(3), TreeNode(1))
        o = TreeNode(2, TreeNode(1), TreeNode(3))
        s.recoverTree(i)
        self.assertEqual(i, o)

if __name__ == '__main__':
    unittest.main(verbosity=2)