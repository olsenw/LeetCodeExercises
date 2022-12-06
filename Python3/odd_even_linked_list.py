# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def list(self):
        head = self
        s = []
        while head:
            s.append(head.val)
            head = head.next
        return s

class Solution:
    '''
    Given the head of singly linked list, group all the nodes with odd indices
    together followed by the nodes with even indices, and return the reordered
    list.

    The first node is considered odd, and the second node is even, and so on.

    Note that the relative order inside both the even and odd groups should
    remain as it was in the input.

    Solve the problem is O(1) extra space complexity and O(n) time complexity.
    '''
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oh, eh = ListNode(), ListNode()
        o, e = oh, eh
        odd = True
        while head:
            n = head.next
            head.next = None
            if odd:
                o.next = head
                o = o.next
            else:
                e.next = head
                e = e.next
            odd = not odd
            head = n
        o.next = eh.next
        return oh.next

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
        o = 5
        self.assertEqual(s.oddEvenList(i).list(), o)

    def test_two(self):
        s = Solution()
        i = ListNode(2,ListNode(1,ListNode(3,ListNode(5,ListNode(6,ListNode(4,ListNode(7)))))))
        o = 5
        self.assertEqual(s.oddEvenList(i).list(), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)