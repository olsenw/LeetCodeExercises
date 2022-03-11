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
    Given the head of a linked list, rotate the list to right by k
    places.
    '''
    def rotateRight_brute(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        if not len(nodes):
            return None
        k = k % len(nodes)
        nodes[-1].next = nodes[0]
        nodes[-k-1].next = None
        return nodes[-k]

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        curr = head
        last = None
        while curr:
            length += 1
            last = curr
            curr = curr.next
        if not length:
            return None
        k = k % length
        last.next = head
        curr = head
        last = None
        for _ in range(length - k):
            last = curr
            curr = curr.next
        last.next = None
        return curr

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        k = 2
        o = ListNode(4, ListNode(5, ListNode(1, ListNode(2, ListNode(3)))))
        self.assertEqual(s.rotateRight(i,k), o)

    def test_two(self):
        s = Solution()
        i = ListNode(0, ListNode(1, ListNode(2)))
        k = 4
        o = ListNode(2, ListNode(0, ListNode(1)))
        self.assertEqual(s.rotateRight(i,k), o)

    def test_three(self):
        s = Solution()
        i = None
        k = 0
        o = None
        self.assertEqual(s.rotateRight(i,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)