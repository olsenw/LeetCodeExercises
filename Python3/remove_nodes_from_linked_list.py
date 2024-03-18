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
    Given the head of a linked list.

    Remove every node which has a node with a greater value anywhere to the
    right side of it.

    Return the head of the modified linked list.
    '''
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        c = head
        while c:
            l.append(c.val)
            c = c.next
        l = l[::-1]
        m = l[0]
        for i in range(len(l)):
            if l[i] < m:
                l[i] = 0
            else:
                m = l[i]
        head = ListNode()
        c = head
        for n in l[::-1]:
            if n:
                c.next = ListNode(n)
                c = c.next
        return head.next

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,4,5]
        o = 5
        self.assertEqual(s.problem_name(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,4,5]
        o = 5
        self.assertEqual(s.problem_name(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)