# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import math
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
    Given the head of a linked list head, in which each node contains an integer
    value.

    Between every pair of adjacent nodes, insert a new node with a value equal
    to the greatest common divisor of them.

    Return the linked list after insertion.

    The greatest common divisor of two numbers is the largest positive integer
    that evenly divides both numbers.
    '''
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last = None
        curr = head
        while curr.next:
            last = curr
            curr = curr.next
            last.next = ListNode(math.gcd(last.val, curr.val), curr)
        return head

class UnitTesting(unittest.TestCase):
    '''
    Tested on LeetCode
    '''
    pass

if __name__ == '__main__':
    unittest.main(verbosity=2)