# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    '''
    There is a singly-linked list head and node node to be deleted from the
    list.

    Given a node to be deleted. The list is unavailable, only the node to be
    deleted is given.

    All the values of the linked list are unique, and it is guaranteed that the
    given node node is not the last node in the linked list.

    Delete the given node. Note that deleting the node means:
    * The value of the given node should not exist in the linked list.
    * The number of nodes in the linked list should decrease by one.
    * All the values before node should be in the same order.
    * All the values after node should be in the same order.
    '''
    def deleteNode(self, node):
        n = node.next
        node.val = n.val
        node.next = n.next
        del(n)

class UnitTesting(unittest.TestCase):
    '''
    Dumb problem...
    Testing only done on Leetcode.
    '''

if __name__ == '__main__':
    unittest.main(verbosity=2)