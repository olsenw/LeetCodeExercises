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
    Given the head of a sorted linked list, delete all nodes that have 
    duplicate numbers, leaving only distinct numbers from the original
    list. Return the linked list sorted as well.
    '''
    def deleteDuplicates_brute(self, head: Optional[ListNode]) -> Optional[ListNode]:
        from collections import Counter
        c = Counter()
        while head:
            c[head.val] += 1
            head = head.next
        dummy = ListNode()
        d = dummy
        for i in c:
            if c[i] == 1:
                d.next = ListNode(i)
                d = d.next
        return dummy.next

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-101)
        last = None
        curr = dummy
        while head:
            # duplicate node
            if curr.val == head.val:
                while head and curr.val == head.val:
                    head = head.next
                curr = last
            # new node
            last = curr
            curr.next = head
            curr = head
            if head:
                head = head.next
        return dummy.next

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5)))))))
        o = ListNode(1, ListNode(2, ListNode(5)))
        self.assertEqual(s.deleteDuplicates(i), o)

    def test_two(self):
        s = Solution()
        i = ListNode(1, ListNode(1, ListNode(1, ListNode(2, ListNode(3)))))
        o = ListNode(2, ListNode(3))
        self.assertEqual(s.deleteDuplicates(i), o)

    def test_three(self):
        s = Solution()
        i = ListNode(1, ListNode(1))
        o = None
        self.assertEqual(s.deleteDuplicates(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)