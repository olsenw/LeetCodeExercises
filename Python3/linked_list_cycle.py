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
    Given head, the head of a linked list, determine if the linked list
    has a cycle in it.

    There is a cycle in a linked list if there is some node in the list
    that can be reached again by continuously following the next
    pointer. Internally, pos is used to denote the index of the node
    that tail's next pointer is connected to. Note that pos is not
    passed as a parameter.

    Return true if there is a cycle in the linked list. Otherwise,
    return false.
    '''
    def hasCycle_set(self, head: Optional[ListNode]) -> bool:
        nodes = set()
        while head:
            if head in nodes:
                return True
            nodes.add(head)
            head = head.next
        return False

    def hasCycle_pointer(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        i = head
        j = head.next
        while i != j:
            if not j.next or not j.next.next:
                return False
            i = i.next
            j = j.next.next
        return True

    # mutates list by marking visited nodes
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head:
            if head.val == 100001:
                return True
            head.val = 100001
            head = head.next
        return False

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ListNode(3)
        i.next = ListNode(2)
        i.next.next = ListNode(0)
        i.next.next.next = ListNode(4)
        i.next.next.next.next = i.next
        o = True
        self.assertEqual(s.hasCycle(i), o)

    def test_two(self):
        s = Solution()
        i = ListNode(1)
        i.next = ListNode(2)
        i.next.next = i
        o = True
        self.assertEqual(s.hasCycle(i), o)

    def test_three(self):
        s = Solution()
        i = ListNode(1)
        o = False
        self.assertEqual(s.hasCycle(i), o)

    def test_four(self):
        s = Solution()
        i = None
        o = False
        self.assertEqual(s.hasCycle(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)