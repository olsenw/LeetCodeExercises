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
    Given the head of a singly linked list and two integers left and
    right where left <= right, reverse the nodes of the list from
    position left to position right, and return the reversed list.
    '''
    # index list then reverse section
    def reverseBetweens_two_pass(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr = head
        l = [ListNode(0,head)]
        while curr:
            l.append(curr)
            curr = curr.next
        l.append(None)
        pass
        for i in range(right, left, -1):
            l[i].next = l[i-1]
        l[left].next = l[right+1]
        l[left-1].next = l[right]
        return l[0].next

    # based on leetcode iterative solution
    def reverseBetweens_one_pass(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # move pointers until point reverse happens
        curr, prev = head, None
        while left > 1:
            prev = curr
            curr = curr.next
            left -= 1
            right -= 1
        # book keeping for revered section break
        tail, con = curr, prev
        # reverse nodes
        while right:
            third = curr.next
            curr.next = prev
            prev = curr
            curr = third
            right -= 1
        # correct links
        if con:
            con.next = prev
        else:
            head = prev
        tail.next = curr
        return head

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        j = 2
        k = 4
        o = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5)))))
        self.assertEqual(s.reverseBetweens(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = ListNode(5)
        j = 1
        k = 1
        o = ListNode(5)
        self.assertEqual(s.reverseBetweens(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = ListNode(1, ListNode(2, ListNode(3)))
        j = 1
        k = 3
        o = ListNode(3, ListNode(2, ListNode(1)))
        self.assertEqual(s.reverseBetweens(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)