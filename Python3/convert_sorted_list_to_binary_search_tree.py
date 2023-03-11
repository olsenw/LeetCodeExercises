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
    Given the head of a singly linked list where elements are sorted in
    ascending order, convert it to a height-balanced binary search tree.
    '''
    # lazy way, by converting linked list into list(array) and divide/conquer
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        # make a list
        l = []
        i = head
        while i:
            l.append(i.val)
            i = i.next
        def r(start, end):
            if end < start:
                return None
            if start == end:
                return TreeNode(l[start])
            m = (end - start) // 2 + start
            return TreeNode(l[m], r(start, m - 1), r(m + 1, end))
        return r(0, len(l)-1)

class UnitTesting(unittest.TestCase):
    '''
    Tested online
    '''
    pass

if __name__ == '__main__':
    unittest.main(verbosity=2)