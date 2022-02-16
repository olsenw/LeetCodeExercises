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
    
    def __eq__(self, other):
        return self.val == other.val and self.next == other.next

    def __str__(self):
        return f"{self.val}, {self.next}"

class Solution:
    '''
    Given a linked list, swap every two adjacent nodes and return its
    head. Do this without modifying the values in the list's nodes (ie
    onlythe nodes themselves may be changed).
    '''
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        h = head
        n = h.next
        h.next = n.next
        n.next = h
        head = n
        l = h
        while h.next and h.next.next:
            h = h.next
            n = h.next
            h.next = n.next
            n.next = h
            l.next = n
            l = h
        return head

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        o = ListNode(2, ListNode(1, ListNode(4, ListNode(3))))
        self.assertEqual(s.swapPairs(i), o)

    def test_two(self):
        s = Solution()
        i = None
        o = None
        self.assertEqual(s.swapPairs(i), o)

    def test_three(self):
        s = Solution()
        i = ListNode(1)
        o = ListNode(1)
        self.assertEqual(s.swapPairs(i), o)

    def test_four(self):
        s = Solution()
        i = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
        o = ListNode(2, ListNode(1, ListNode(4, ListNode(3, ListNode(6, ListNode(5))))))
        self.assertEqual(s.swapPairs(i), o)

    def test_five(self):
        s = Solution()
        i = ListNode(1, ListNode(2, ListNode(3)))
        o = ListNode(2, ListNode(1, ListNode(3)))
        self.assertEqual(s.swapPairs(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)