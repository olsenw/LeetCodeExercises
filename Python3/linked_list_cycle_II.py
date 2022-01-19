# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    '''
    Given the head of linked list, return the node where the cycle 
    begins. If there is no cycle, return null.

    There is a cycle in a linked list if there is some node in the list
    that can be reached again by continuously following the next 
    pointer. Internally, pos is used to denote the index of the node 
    that tail's next pointer is connected to (0-indexed). It is -1 if
    there is no cycle. Note that pos is not passed as a parameter.

    Do not modify the linked list.
    '''
    # O(n) time
    # O(n) space
    def detectCycle_set(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = head
        s = set()
        while n:
            if n in s:
                return n
            s.add(n)
            n = n.next
        return None

    # O(n + (n-c)*c) time n is num nodes c is length cycle
    #  which boils down to O(n) time (do math...)
    # O(1) space
    def detectCycle_const(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next and head.next.next:
            i = head.next
            j = head.next.next
            while i != j:
                if j.next and j.next.next:
                    i = i.next
                    j = j.next.next
                else:
                    # j ran off list w/o cycle
                    return None
            # cycle starts at/before i
            h = head
            j = j.next
            while h != j:
                if i == j:
                    h = h.next
                j = j.next
            return h
        # list is one node, or 2nd node does not cycle
        return None

    # breaks rule about modifying the list...
    # based on idea from discussion post
    # https://leetcode.com/problems/linked-list-cycle-ii/discuss/1700902/O(n)-Time-O(1)-Space-One-time-Linked-List-walk-through-solution
    # O(n) time
    # O(1) space
    def detectCycle_modify(self, head: Optional[ListNode]) -> Optional[ListNode]:
        while head:
            if head.val > 10**5:
                return head
            head.val = 10**5 + 1
            head = head.next
        return None


class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ListNode(3)
        i.next = ListNode(2)
        i.next.next = ListNode(0)
        i.next.next.next = ListNode(-4)
        i.next.next.next.next = i.next
        o = i.next
        self.assertEqual(s.detectCycle_set(i), o)
        self.assertEqual(s.detectCycle_const(i), o)
        self.assertEqual(s.detectCycle_modify(i), o)

    def test_two(self):
        s = Solution()
        i = ListNode(1)
        i.next = ListNode(2)
        i.next.next = i
        o = i
        self.assertEqual(s.detectCycle_set(i), o)
        self.assertEqual(s.detectCycle_const(i), o)
        self.assertEqual(s.detectCycle_modify(i), o)

    def test_three(self):
        s = Solution()
        i = ListNode(1)
        o = None
        self.assertEqual(s.detectCycle_set(i), o)
        self.assertEqual(s.detectCycle_const(i), o)
        self.assertEqual(s.detectCycle_modify(i), o)

    def test_four(self):
        s = Solution()
        i = ListNode(1)
        o = None
        self.assertEqual(s.detectCycle_set(i), o)
        self.assertEqual(s.detectCycle_const(i), o)
        self.assertEqual(s.detectCycle_modify(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)