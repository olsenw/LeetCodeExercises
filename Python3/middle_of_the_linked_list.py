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

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = False
        mid = head
        end = head
        while end.next:
            odd = not odd
            if odd:
                mid = mid.next
            end = end.next
        return mid

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        o = ListNode(3, ListNode(4, ListNode(5)))
        a = s.middleNode(i)
        while a.next and o.next: 
            self.assertEqual(a.val, o.val)
            a = a.next
            o = o.next
        self.assertEqual(a.val, o.val)
        self.assertIsNone(a.next)
        self.assertIsNone(o.next)

    def test_two(self):
        s = Solution()
        i = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
        o = ListNode(4, ListNode(5, ListNode(6)))
        a = s.middleNode(i)
        while a.next and o.next: 
            self.assertEqual(a.val, o.val)
            a = a.next
            o = o.next
        self.assertEqual(a.val, o.val)
        self.assertIsNone(a.next)
        self.assertIsNone(o.next)

    def test_three(self):
        s = Solution()
        i = ListNode(1, ListNode(2))
        o = ListNode(2)
        a = s.middleNode(i)
        while a.next and o.next: 
            self.assertEqual(a.val, o.val)
            a = a.next
            o = o.next
        self.assertEqual(a.val, o.val)
        self.assertIsNone(a.next)
        self.assertIsNone(o.next)

    def test_four(self):
        s = Solution()
        i = ListNode(1)
        o = ListNode(1)
        a = s.middleNode(i)
        while a.next and o.next: 
            self.assertEqual(a.val, o.val)
            a = a.next
            o = o.next
        self.assertEqual(a.val, o.val)
        self.assertIsNone(a.next)
        self.assertIsNone(o.next)

if __name__ == '__main__':
    unittest.main(verbosity=2)