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

class Solution:
    '''
    Given the head of a non-empty linked list representing a non-negative
    integer without leading zeros.

    Return the head of the linked list after doubling it.
    '''
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = []
        head = ListNode(0,head)
        curr = head
        while curr:
            s.append(curr)
            curr = curr.next
        carry = 0
        while s:
            carry, s[-1].val = divmod(s[-1].val * 2 + carry, 10)
            s.pop()
        return head if head.val else head.next

    '''
    Could have played games with the next pointer if O(1) space was needed.
    '''
class UnitTesting(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main(verbosity=2)