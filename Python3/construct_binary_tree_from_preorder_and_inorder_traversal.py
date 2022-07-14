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
        return self.val == other.val and self.left == other.left and self.right == other.right
    def preorder(self):
        v = [self.val]
        l = self.left.preorder() if self.left else []
        r = self.right.preorder() if self.right else []
        return v + l + r
    def inorder(self):
        v = [self.val]
        l = self.left.inorder() if self.left else []
        r = self.right.inorder() if self.right else []
        return l + v + r

class Solution:
    '''
    Given two integer arrays preorder and inorder where preorder is the
    preorder traversal of a binary tree and inorder is the traversal of
    the same tree, construct and return the binary tree.
    '''
    # based on leetcode solution
    # O(n) time
    # O(n) space
    # if know where the root is located in the inorder array, know all
    # values that go left (left of root index) and values that go right
    # (right of root index)
    # preorder tells us what the root index must be
    # by recursively building on subarrays of inorder while iterating
    # the root values in preorder can get tree
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # hash map of value's location in inorder
        inode = {io:i for i,io in enumerate(inorder)}
        # what index in preorder is being used as root
        pindex = 0
        # recursive function to build tree
        def f(l, r):
            nonlocal pindex
            # subarray is empty (ie no tree node)
            if l > r:
                return None
            # what is root of this binary tree
            value = preorder[pindex]
            root = TreeNode(value)
            # set next root (slick trick due to how tree built)
            pindex += 1
            # create left of tree
            root.left = f(l, inode[value] - 1)
            # create right of tree
            root.right = f(inode[value] + 1, r)
            return root
        return f(0, len(inorder)-1)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,9,20,15,7]
        j = [9,3,15,20,7]
        o = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        self.assertEqual(s.buildTree(i,j), o)

    def test_two(self):
        s = Solution()
        i = [-1]
        j = [-1]
        o = TreeNode(-1)
        self.assertEqual(s.buildTree(i,j), o)

    # def test_order(self):
    #     t = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    #     self.assertEqual(t.preorder(), [3,9,20,15,7])
    #     self.assertEqual(t.inorder(), [9,3,15,20,7])
    #     t = TreeNode(-1)
    #     self.assertEqual(t.preorder(), [-1])
    #     self.assertEqual(t.inorder(), [-1])
    #     t = TreeNode('a', TreeNode('b', None, TreeNode('d', TreeNode('f'), TreeNode('g'))), TreeNode('c', TreeNode('e', None, TreeNode('h', None, TreeNode('i')))))
    #     self.assertEqual(t.preorder(), ['a','b','d','f','g','c','e','h','i'])
    #     self.assertEqual(t.inorder(), ['b','f','d','g','a','e','h','i','c'])

if __name__ == '__main__':
    unittest.main(verbosity=2)