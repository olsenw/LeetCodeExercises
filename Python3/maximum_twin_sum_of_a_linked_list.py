# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
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
    In a linked list of size n, where n is even, the ith node (0-indexed) of the
    linked list is known as the twin of the (n-1-i)th node if 
    0 <= i <= (n / 2) - 1.

    The twin sum is defined as the sum of a node and its twin.

    Given the head of a linked list of even length, return the maximum twin sum
    of the linked list.
    '''
    def pairSum(self, head: Optional[ListNode]) -> int:
        d = deque()
        while head:
            d.append(head.val)
            head = head.next
        answer = 0
        while d:
            answer = max(answer, d.popleft() + d.pop())
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ListNode(5, ListNode(4, ListNode(2, ListNode(1))))
        o = 6
        self.assertEqual(s.pairSum(i), o)

    def test_two(self):
        s = Solution()
        i = ListNode(4, ListNode(2, ListNode(2, ListNode(3))))
        o = 7
        self.assertEqual(s.pairSum(i), o)

    def test_three(self):
        s = Solution()
        i = ListNode(1, ListNode(100000))
        o = 100001
        self.assertEqual(s.pairSum(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)