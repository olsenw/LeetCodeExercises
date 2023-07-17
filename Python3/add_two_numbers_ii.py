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
    def __eq__(self, obj) -> bool:
        return self.val == obj.val and self.next == obj.next

class Solution:
    '''
    Given two non-empty linked lists representing two non-negative integers. The
    most significant digit comes first and each of their nodes contains a single
    digit. Add the two numbers and return the sum as a linked list.

    The test cases are designed such that the two numbers do not contain any
    leading zeros, except the number 0 itself.
    '''
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(root: ListNode):
            prev = None
            curr = root
            while curr is not None:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        l1 = reverse(l1)
        l2 = reverse(l2)
        answer = None
        a = l1
        b = l2
        c = 0
        # while a is not None and b is not None:
        #     v = a.val + b.val + c
        #     answer = ListNode(v % 10, answer)
        #     a = a.next
        #     b = b.next
        #     c = v // 10
        # while a is not None:
        #     v = a.val + c
        #     answer = ListNode(v % 10, answer)
        #     a = a.next
        #     c = v // 10
        # while b is not None:
        #     v = b.val + c
        #     answer = ListNode(v % 10, answer)
        #     b = b.next
        #     c = v // 10
        while a or b:
            if a:
                c += a.val
                a = a.next
            if b:
                c += b.val
                b = b.next
            answer = ListNode(c % 10, answer)
            c //= 10
        if c == 1:
            answer = ListNode(1, answer)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ListNode(7, ListNode(2, ListNode(4, ListNode(3))))
        j = ListNode(5, ListNode(6, ListNode(4)))
        o = ListNode(7, ListNode(8, ListNode(0, ListNode(7))))
        self.assertEqual(s.addTwoNumbers(i,j), o)

    def test_two(self):
        s = Solution()
        i = ListNode(2, ListNode(4, ListNode(3)))
        j = ListNode(5, ListNode(6, ListNode(4)))
        o = ListNode(8, ListNode(0, ListNode(7)))
        self.assertEqual(s.addTwoNumbers(i,j), o)

    def test_three(self):
        s = Solution()
        i = ListNode(0)
        j = ListNode(0)
        o = ListNode(0)
        self.assertEqual(s.addTwoNumbers(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)