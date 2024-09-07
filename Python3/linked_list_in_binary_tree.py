# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
    Given a binary tree root and a linked list with head as the first node.

    Return True if all the elements in the linked list starting from the head
    correspond to some downward path connected in the binary tree otherwise
    return False.

    In this context downward path means a path that starts at some node and goes
    downwards.
    '''
    def isSubPath_incomplete(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if head is None:
            return True
        if root is None or head.val != root.val:
            return False
        return self.isSubPath(head.next, root.left) or self.isSubPath(head.next, root.right)

    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(lNode, tNode):
            if lNode is None:
                return True
            if tNode is None or lNode.val != tNode.val:
                return False
            return dfs(lNode.next, tNode.left) or dfs(lNode.next, tNode.right)
        if root is None:
            return False
        if head.val == root.val and dfs(head, root):
            return True
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

class UnitTesting(unittest.TestCase):
    '''
    Tested on Leetcode
    '''
    pass

if __name__ == '__main__':
    unittest.main(verbosity=2)