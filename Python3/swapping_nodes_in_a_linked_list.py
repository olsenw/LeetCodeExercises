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
        if type(other) == ListNode:
            return self.val == other.val and self.next == other.next
        return False

class Solution:
    '''
    Given the head of a linked list, and an integer k.

    Return the head of the linked list after swapping the values of the
    kth node from the beginning and the kth node from the end (note the
    list is 1-indexed).
    '''
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        a = head
        for _ in range(k-1):
            a = a.next
        i = a
        j = head
        while i.next:
            i = i.next
            j = j.next
        a.val, j.val = j.val, a.val
        return head

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        j = 2
        o = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5)))))
        self.assertEqual(s.swapNodes(i,j), o)

    def test_two(self):
        s = Solution()
        i = ListNode(7, ListNode(9, ListNode(6, ListNode(6, ListNode(7, ListNode(8, ListNode(3, ListNode(0, ListNode(9, ListNode(5))))))))))
        j = 5
        o = ListNode(7, ListNode(9, ListNode(6, ListNode(6, ListNode(8, ListNode(7, ListNode(3, ListNode(0, ListNode(9, ListNode(5))))))))))
        self.assertEqual(s.swapNodes(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)