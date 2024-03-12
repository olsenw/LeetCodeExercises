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
    def __eq__(self, __value: object) -> bool:
        if self is None or __value is None:
            return self is None and __value is None
        return self.val == __value.val and self.next == __value.next

class Solution:
    '''
    Given the head of a linked list, repeatedly delete consecutive sequences of
    nodes that sum to 0 until there are no such sequences.

    After doing so, return the head of the final linked list. Any such answer
    may be returned.
    '''
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = []
        c = head
        while c:
            a.append(c.val)
            c = c.next
        
        c = ListNode(0)
        answer = c

        i = 0
        while i < len(a):
            s = 0
            for j in range(i, len(a)):
                s += a[j]
                if s == 0:
                    i = j + 1
                    break
            if s != 0:
                c.next = ListNode(a[i])
                c = c.next
                i += 1

        return answer.next

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ListNode(1, ListNode(2, ListNode(-3, ListNode(3, ListNode(1)))))
        o = ListNode(3, ListNode(1))
        self.assertEqual(s.removeZeroSumSublists(i), o)

    def test_two(self):
        s = Solution()
        i = ListNode(1, ListNode(2, ListNode(3, ListNode(-3, ListNode(4)))))
        o = ListNode(1,ListNode(2, ListNode(4)))
        self.assertEqual(s.removeZeroSumSublists(i), o)

    def test_three(self):
        s = Solution()
        i = ListNode(1, ListNode(2, ListNode(3, ListNode(-3, ListNode(-2)))))
        o = ListNode(1)
        self.assertEqual(s.removeZeroSumSublists(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)