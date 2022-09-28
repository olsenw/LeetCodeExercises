# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from email import header
from multiprocessing import dummy
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

class Solution:
    '''
    Given the head of a linked list, remove the nth node from the end of the
    list and return its head.
    '''
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        c = dummy
        for _ in range(n):
            c = c.next
        l = dummy
        c = c.next
        while c:
            c = c.next
            l = l.next
        l.next = l.next.next
        return dummy.next

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        j = 2
        o = ListNode(1, ListNode(2, ListNode(3, ListNode(5))))
        self.assertEqual(s.removeNthFromEnd(i,j), o)

    def test_two(self):
        s = Solution()
        i = ListNode(1)
        j = 1
        o = None
        self.assertEqual(s.removeNthFromEnd(i,j), o)

    def test_three(self):
        s = Solution()
        i = ListNode(1, ListNode(2))
        j = 1
        o = ListNode(1)
        self.assertEqual(s.removeNthFromEnd(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)