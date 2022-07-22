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

    @staticmethod
    def fromList(values):
        head = curr = ListNode()
        for v in values:
            curr.next = ListNode(v)
            curr = curr.next
        return head.next

    def toList(self):
        values = []
        curr = self
        while curr:
            values.append(curr.val)
            curr = curr.next
        return values

class Solution:
    '''
    Given the head of a linked list and a value x, partition it such 
    that all nodes less than x come before nodes greater than or equal
    to x.

    The relative order of the nodes in each partition should be 
    preserved.
    '''
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lesser = l = ListNode()
        greater = g = ListNode()
        while head:
            if head.val >= x:
                g.next = head
                g = g.next
            else:
                l.next = head
                l = l.next
            head = head.next
        g.next = None
        l.next = greater.next
        return lesser.next

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ListNode.fromList([1,4,3,2,5,2])
        j = 3
        o = [1,2,2,4,3,5]
        self.assertEqual(s.partition(i,j).toList(), o)

    def test_two(self):
        s = Solution()
        i = ListNode.fromList([2,1])
        j = 2
        o = [1,2]
        self.assertEqual(s.partition(i,j).toList(), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)