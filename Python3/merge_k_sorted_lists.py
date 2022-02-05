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

    # https://stackoverflow.com/questions/390250/elegant-ways-to-support-equivalence-equality-in-python-classes
    def __eq__(self, other):
        # overides defult implentation
        if isinstance(other, ListNode):
            return self.val == other.val and self.next == other.next
        return NotImplemented

class Solution:
    '''
    Given an array of k linked-lists lists, each linked-list is sorted
    in ascending order.

    Merge all the linked-lists into one sorted linked-list and return
    it.
    '''
    def mergeKLists_works(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # create a min heap for aggregating lists (value, list from)
        import heapq
        h = [(lists[i].val, i) for i in range(len(lists)) if lists[i]]
        heapq.heapify(h)
        # dummy node to build off of
        root = ListNode()
        # current node
        n = root
        while len(h):
            v,i = h[0]
            n.next = ListNode(v)
            n = n.next
            lists[i] = lists[i].next
            if lists[i]:
                heapq.heappushpop(h,(lists[i].val, i))
            else:
                heapq.heappop(h)
        return root.next

class UnitTesting(unittest.TestCase):
    def listIt(self, l):
        if len(l):
            root = ListNode(l[0])
            n = root
            for i in l[1:]:
                n.next = ListNode(i)
                n = n.next
            return root
        return None

    def test_one(self):
        s = Solution()
        i = [self.listIt(i) for i in [[1,4,5],[1,3,4],[2,6]]]
        o = self.listIt([1,1,2,3,4,4,5,6])
        self.assertEqual(s.mergeKLists_works(i), o)

    def test_two(self):
        s = Solution()
        i = []
        o = None
        self.assertEqual(s.mergeKLists_works(i), o)

    def test_three(self):
        s = Solution()
        i = [None]
        o = None
        self.assertEqual(s.mergeKLists_works(i), o)

    # def test_four(self):
    #     s = Solution()
    #     i = [self.listIt(i) for i in [j for j in range(1,501)] * 1000]
    #     o = self.listIt([j for i in range(1000) for j in range(1,501)])
    #     self.assertEqual(s.mergeKLists_works(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)