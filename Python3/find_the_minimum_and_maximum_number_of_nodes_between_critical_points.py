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
    def fromList(l: List[int]):
        h = ListNode()
        c = h
        for i in l:
            c.next = ListNode(i)
            c = c.next
        return h.next

class Solution:
    '''
    A critical point in a linked list is defined as either a local maxima or a
    local minima.

    A node is a local maxima if the current node has a value strictly greater
    than the previous node and the next node.

    A node is a local minima if the current node has a value strictly smaller
    than the previous node and the next node.

    Note that a node can only be a local maxima/minima if there exists both a
    previous node and a next node.

    Given a linked list head, return an array of length 2 containing
    [minDistance, maxDistance] where minDistance is the minimum distance between
    any two distinct critical points and maxDistance is the maximum distance
    between any two distinct critical points. If there are fewer than two
    critical points, return [-1, -1].
    '''
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        l, c, i = head, head.next, 1
        if not c.next:
            return [-1, -1]
        n = c.next
        local = []
        while n:
            if l.val < c.val > n.val:
                local.append(i)
            if l.val > c.val < n.val:
                local.append(i)
            l = c
            c = n
            n = n.next
            i += 1
        if len(local) < 2:
            return [-1, -1]
        return [min(local[i] - local[i-1] for i in range(1, len(local))), local[-1] - local[0]]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ListNode.fromList([3,1])
        o = [-1,-1]
        self.assertEqual(s.nodesBetweenCriticalPoints(i), o)

    def test_two(self):
        s = Solution()
        i = ListNode.fromList([5,3,1,2,5,1,2])
        o = [1,3]
        self.assertEqual(s.nodesBetweenCriticalPoints(i), o)

    def test_three(self):
        s = Solution()
        i = ListNode.fromList([1,3,2,2,3,2,2,2,7])
        o = [3,3]
        self.assertEqual(s.nodesBetweenCriticalPoints(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)