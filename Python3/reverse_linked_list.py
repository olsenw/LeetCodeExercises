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

class Solution:
    '''
    Given the head of a singly linked list, reverse the list, and return the
    reversed list.
    '''
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        last = head
        curr = head.next
        last.next = None
        while curr.next:
            next = curr.next
            curr.next = last
            last = curr
            curr = next
        curr.next = last
        return curr

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        o = 5
        self.assertEqual(s.reverseList(i), o)

    def test_two(self):
        s = Solution()
        i = None
        o = None
        self.assertEqual(s.reverseList(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)