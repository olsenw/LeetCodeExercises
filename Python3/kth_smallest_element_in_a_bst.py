# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Optional

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
    Given the root of a binary search tree, and an integer k, return the
    kth smallest value (1-indexed) of all the values of the nodes in the
    tree.
    '''
    # iterative in-order traversal looked from GeeksforGeeks
    # https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion/
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        a = 0
        stack = deque()
        curr = root
        while k > 0:
            if curr:
                stack.append(curr)
                curr = curr.left
            elif stack:
                curr = stack.pop()
                a = curr.val
                k -= 1
                curr = curr.right
            else:
                break
        return a
    
    '''
    Follow up: If the BST is modified often (ie insert/delete) and 
    required to find the kth smallest frequently, how could it be
    optimized?

    Also have the nodes in a sorted doubled linked list which is
    maintained during insert/delete operaions. Could then traverse the
    list to find kth smallest.

    An alternate idea is to record at each node the number of nodes
    contained in the left subtree.
    '''

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
        j = 1
        o = 1
        self.assertEqual(s.kthSmallest(i, j), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(8))
        j = 3
        o = 3
        self.assertEqual(s.kthSmallest(i, j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)