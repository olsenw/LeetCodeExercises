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

    def __eq__(self, other: 'ListNode') -> bool:
        a = []
        c = self
        while c:
            a.append(c.val)
            c = c.next
        b = []
        c = other
        while c:
            b.append(c.val)
            c = c.next
        return a == b

class Solution:
    '''
    Given two linked lists: list1 and list2 of size n and m respectively.

    Remove list1's nodes from the ath node to the bth node, and put list2 in
    their place.

    Build the result and return its head.
    '''
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        x,y = None, None
        curr = list1
        for _ in range(a-1):
            curr = curr.next
        x = curr
        for _ in range(b-a+2):
            curr = curr.next
        y = curr
        curr = list2
        last = None
        while curr:
            last = curr
            curr = curr.next
        x.next = list2
        last.next = y
        return list1

class UnitTesting(unittest.TestCase):
    def make_list(self, values):
        h = ListNode()
        c = h
        for v in values:
            c.next = ListNode(v)
            c = c.next
        return h.next
    def to_list(self, node):
        a = []
        while node:
            a.append(node.val)
            node = node.next
        return a

    def test_one(self):
        s = Solution()
        i = self.make_list([10,1,13,6,9,5])
        j = 3
        k = 4
        l = self.make_list([1000000,1000001,1000002])
        o = [10,1,13,1000000,1000001,1000002,5]
        self.assertEqual(self.to_list(s.mergeInBetween(i,j,k,l)), o)

    def test_two(self):
        s = Solution()
        i = self.make_list([0,1,2,3,4,5,6])
        j = 2
        k = 5
        l = self.make_list([1000000,1000001,1000002,1000003,1000004])
        o = [0,1,1000000,1000001,1000002,1000003,1000004,6]
        self.assertEqual(self.to_list(s.mergeInBetween(i,j,k,l)), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)