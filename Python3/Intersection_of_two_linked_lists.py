# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    '''
    Given the heads of two singly linked-lists headA and headB, return
    the node at which the two lists intersect. If the two linked lists
    have no intersection at all, return null.

    Note: the linked lists must retain their original structure after
    the function returns.
    '''

    # O(m * n) time
    # O(1) space
    def getIntersectionNode_mn_time(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = headA
        while a:
            b = headB
            while b:
                if a is b:
                    return b
                b = b.next
            a = a.next
        return None

    # O(m + n) time
    # O(m) space
    def getIntersectionNode_m_space(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        s = set()
        h = headA
        while h:
            s.add(h)
            h = h.next
        h = headB
        while h:
            if h in s:
                return h
            h = h.next
        return None

    # O(m + m + n) time
    # O(1) space
    # abuses the constraint that 1 <= Node.val <= 10^6
    def getIntersectionNode_marking(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # mark nodes in list A
        h = headA
        while h:
            h.val *= -1
            h = h.next
        # look for a marked node in list B
        i = headB
        while i:
            if i.val < 0:
                break
            i = i.next
        # fix list A
        h = headA
        while h:
            h.val *= -1
            h = h.next
        return i

    # O(m + n) time
    # O(1) space
    # based on idea by ezradiniz
    # https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/2116135/Python-or-O(1)-space-or-Diff-Length-or-Easy
    def getIntersectionNode_lengths(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # get length of linked list
        def length(node):
            c = 0
            while node:
                c += 1
                node = node.next
            return c
        # get lengths of list A and list B
        a, b = length(headA), length(headB)
        # how many elements to skip in longer list
        skip = abs(a - b)
        # determine which list to skip elements in
        if b > a:
            headA, headB = headB, headA
        # skip ahead
        for _ in range(skip):
            headA = headA.next
        # advance until none or intersection
        while headA is not headB:
            headA = headA.next
            headB = headB.next
        # return answer
        return headA

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ListNode(8, ListNode(4, ListNode(5)))
        a = ListNode(4, ListNode(1, i))
        b = ListNode(5, ListNode(6, ListNode(1, i)))
        self.assertEqual(id(s.getIntersectionNode(a,b)), id(i))

    def test_two(self):
        s = Solution()
        i = ListNode(2, ListNode(4))
        a = ListNode(1,ListNode(9, ListNode(2, i)))
        b = ListNode(3, i)
        self.assertEqual(id(s.getIntersectionNode(a,b)), id(i))

    def test_three(self):
        s = Solution()
        a = ListNode(2, ListNode(6, ListNode(4)))
        b = ListNode(1, ListNode(5))
        self.assertEqual(s.getIntersectionNode(a,b), None)

if __name__ == '__main__':
    unittest.main(verbosity=2)