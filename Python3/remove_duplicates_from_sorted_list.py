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
    def __eq__(self, __value: object) -> bool:
        return self.val == __value.val and self.next == __value.next

class Solution:
    '''
    Given the head of a sorted linked list, delete all duplicates such that each
    element appears only once. Return the linked list in sorted order as well.
    '''
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        current:Optional[ListNode] = head.next
        last = head
        while current:
            if current.val == last.val:
                last.next = current.next
            else:
                last = current
            current = current.next
        return head

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ListNode(1,ListNode(1, ListNode(2)))
        o = ListNode(1, ListNode(2))
        self.assertEqual(s.deleteDuplicates(i), o)

    def test_two(self):
        s = Solution()
        i = ListNode(1,ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
        o = ListNode(1,ListNode(2, ListNode(3)))
        self.assertEqual(s.deleteDuplicates(i), o)

    def test_three(self):
        s = Solution()
        i = None
        o = None
        self.assertEqual(s.deleteDuplicates(i), o)

    def test_four(self):
        s = Solution()
        i = ListNode(1)
        o = ListNode(1)
        self.assertEqual(s.deleteDuplicates(i), o)

    def test_five(self):
        s = Solution()
        i = ListNode(1)
        o = ListNode(1)
        self.assertEqual(s.deleteDuplicates(i), o)

    def test_six(self):
        s = Solution()
        i = ListNode(1,ListNode(1,ListNode(1)))
        o = ListNode(1)
        self.assertEqual(s.deleteDuplicates(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)