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

class Solution:
    '''
    Given the heads of two sorted linked lists, list1 and list2.

    Merge the two lists into a sorted linked list. Return the head of 
    the combined list.
    '''
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        d = dummy
        i = list1
        j = list2
        # merge
        while i and j:
            if i.val < j.val:
                d.next = i
                i = i.next
            else:
                d.next = j
                j = j.next
            d = d.next
        # trailing list 1
        while i:
            d.next = i
            i = i.next
            d = d.next
        # trailing list 2
        while j:
            d.next = j
            j = j.next
            d = d.next
        # return head of merged list
        return dummy.next

    def mergeTwoLists_refined(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        d = dummy
        # merge sorted
        while list1 and list2:
            if list1.val < list2.val:
                d.next = list1
                list1 = list1.next
            else:
                d.next = list2
                list2 = list2.next
            d = d.next
        # trailing
        d.next = list1 if list1 else list2
        return dummy.next

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ListNode(1, ListNode(2, ListNode(4)))
        j = ListNode(1, ListNode(3, ListNode(4)))
        o = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4))))))
        self.assertEqual(s.mergeTwoLists_refined(i,j), o)

    def test_two(self):
        s = Solution()
        i = None
        j = None
        o = None
        self.assertEqual(s.mergeTwoLists_refined(i,j), o)

    def test_three(self):
        s = Solution()
        i = None
        j = ListNode()
        o = ListNode()
        self.assertEqual(s.mergeTwoLists_refined(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)