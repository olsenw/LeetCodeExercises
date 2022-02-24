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
        if isinstance(other, ListNode):
            return self.val == other.val and self.next == other.next
        return False

class Solution:
    '''
    Given the head of a linked list return the list after sorting it in
    ascending order.
    '''
    # pretty brute force (recreates list after sorting values)
    def sortList_n_space(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        n = head
        while n:
            l.append(n.val)
            n = n.next
        h = ListNode()
        n = h
        for s in sorted(l):
            n.next = ListNode(s)
            n = n.next
        return h.next

    # insertion sort (O(n^2) time)
    # timesout due to large problem space
    def sortList_insertion_constant_space(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = head
        d = ListNode(-10**5 - 1)
        while n:
            i = d
            while i.next and i.next.val < n.val:
                i = i.next
            i.next, n.next, n = (n, i.next, n.next)
        return d.next

    '''
    The best answer is to do a merge sort. Merge sort is preferred over
    Quick sort because it does not require random memory accesses to
    work.

    Code is somewhat involved however... so did not type it out

    Leetcode solution explains how to do bottom up merge sort that
    requires constant space.

    https://leetcode.com/problems/sort-list/solution/
    '''

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
        o = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        self.assertEqual(s.sortList_n_space(i), o)
        self.assertEqual(s.sortList_insertion_constant_space(i), o)

    def test_two(self):
        s = Solution()
        i = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode()))))
        o = ListNode(-1, ListNode(0, ListNode(3, ListNode(4, ListNode(5)))))
        self.assertEqual(s.sortList_n_space(i), o)
        self.assertEqual(s.sortList_insertion_constant_space(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)