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
    Given two non-empty linked lists representing two non-negative
    integers. The digits are stored in reverse order, and each of their
    nodes contains a single digit. Add the two numbers and return the
    sum as a linked list.

    The two numbers do not contain any leading zeros, except the number
    zero itself.
    '''
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 and l2:
            carry += l1.val + l2.val
            curr.next = ListNode(carry % 10)
            carry //= 10
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        l = l1 or l2
        while l and carry:
            carry += l.val
            curr.next = ListNode(carry % 10)
            carry //= 10
            curr = curr.next
            l = l.next
        if carry:
            curr.next = ListNode(carry)
        else:
            curr.next = l
        return dummy.next

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        # 342 in reverse order
        i = ListNode(2, ListNode(4, ListNode(3)))
        # 465 in reverse order
        j = ListNode(5, ListNode(6, ListNode(4)))
        # 807 n reverse order
        o = ListNode(7, ListNode(0, ListNode(8)))
        self.assertEqual(s.addTwoNumbers(i,j), o)

    def test_two(self):
        s = Solution()
        # 342 in reverse order
        i = ListNode(0)
        # 465 in reverse order
        j = ListNode(0)
        # 807 n reverse order
        o = ListNode(0)
        self.assertEqual(s.addTwoNumbers(i,j), o)

    def test_three(self):
        s = Solution()
        # 342 in reverse order
        i = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
        # 465 in reverse order
        j = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
        # 807 n reverse order
        o =  ListNode(8, ListNode(9, ListNode(9, ListNode(9, ListNode(0, ListNode(0, ListNode(0, ListNode(1))))))))
        self.assertEqual(s.addTwoNumbers(i,j), o)

    def test_four(self):
        s = Solution()
        # 342 in reverse order
        i = ListNode(1, ListNode(0, ListNode(1)))
        # 465 in reverse order
        j = ListNode(1)
        # 807 n reverse order
        o = ListNode(2, ListNode(0, ListNode(1)))
        self.assertEqual(s.addTwoNumbers(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)