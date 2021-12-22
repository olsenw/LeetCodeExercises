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

class Solution:
    '''
    Given the head of a singly linked-list, which can be represented as:
    L0 -> L1 -> L2 -> ... -> Ln-1 -> Ln
    
    Reorder the list to be in the following form:
    L0 -> Ln-1 -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...

    Do not modify the values of the list's nodes, only the pointers.
    '''

    # This one will time out when submitted
    def reorderList_slow(self, head: Optional[ListNode]) -> None:
        n = head
        while n.next:
            l = n.next
            # find next to last element in list
            while l.next and l.next.next:
                l = l.next
            if l.next is None:
                return
            last = l.next
            l.next = None
            temp = n.next
            n.next = last
            last.next = temp
            if n.next and n.next.next:
                n = n.next.next
            else:
                return

    def reorderList_inplace(self, head: Optional[ListNode]) -> None:
        # find length of list
        length = 0
        n = head
        while n.next:
            length += 1
            n = n.next
        else:
            length += 1
        
        # base cases for single and two element lists
        if length <= 2:
            return
        
        # find middle of list
        n = length // 2
        if length % 2:
            # length is odd left half 1 longer than right half
            n += 1
        middle = head
        n -= 1
        while n:
            middle = middle.next
            n -= 1
        
        # divide list
        tmp = middle.next
        middle.next = None
        middle = tmp

        # reverse 2nd half of list
        last = None
        while middle.next:
            tmp = middle.next
            middle.next = last
            last = middle
            middle = tmp
        else:
            middle.next = last
        
        # recombine lists
        n = head
        while n.next and middle.next:
            # temps for swaping
            tmp = n.next
            mtmp = middle.next
            # updating pointers
            n.next = middle
            middle.next = tmp
            # next iteration
            n = tmp
            middle = mtmp
        else:
            tmp = n.next
            n.next = middle
            if tmp:
                middle.next = tmp
        pass

    def reorderList_deque(self, head: Optional[ListNode]) -> None:
        from collections import deque
        d = deque()
        n = head
        # put all elements on double sided queue
        while n.next:
            d.append(n)
            n = n.next
        else:
            d.append(n)
        # pop elements off into new order
        dummy = ListNode(0)
        while d:
            f = d.popleft()
            dummy.next = f
            if d:
                b = d.pop()
                b.next = None
                f.next = b
                dummy = b
            else:
                f.next = None

class UnitTesting(unittest.TestCase):
    def compare(self, u: Optional[ListNode], o: Optional[ListNode]):
        ut = u
        ot = o
        while ut and ot:
            # compare elements
            self.assertEqual(ut.val, ot.val)
            ut = ut.next
            ot = ot.next
        else:
            # check they are both None (ie no more elements)
            self.assertEqual(ut, None)
            self.assertEqual(ot, None)

    def test_one_slow(self):
        u = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        o = ListNode(1, ListNode(4, ListNode(2, ListNode(3))))
        s = Solution()
        s.reorderList_slow(u)
        self.compare(u, o)

    def test_two_slow(self):
        u = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        o = ListNode(1, ListNode(5, ListNode(2, ListNode(4, ListNode(3)))))
        s = Solution()
        s.reorderList_slow(u)
        self.compare(u, o)

    def test_one_inplace(self):
        u = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        o = ListNode(1, ListNode(4, ListNode(2, ListNode(3))))
        s = Solution()
        s.reorderList_inplace(u)
        self.compare(u, o)

    def test_two_inplace(self):
        u = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        o = ListNode(1, ListNode(5, ListNode(2, ListNode(4, ListNode(3)))))
        s = Solution()
        s.reorderList_inplace(u)
        self.compare(u, o)

    def test_three_inplace(self):
        u = ListNode(1)
        o = ListNode(1)
        s = Solution()
        s.reorderList_inplace(u)
        self.compare(u, o)

    def test_four_inplace(self):
        u = ListNode(1, ListNode(2))
        o = ListNode(1, ListNode(2))
        s = Solution()
        s.reorderList_inplace(u)
        self.compare(u, o)

    def test_one_deque(self):
        u = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        o = ListNode(1, ListNode(4, ListNode(2, ListNode(3))))
        s = Solution()
        s.reorderList_deque(u)
        self.compare(u, o)

    def test_two_deque(self):
        u = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        o = ListNode(1, ListNode(5, ListNode(2, ListNode(4, ListNode(3)))))
        s = Solution()
        s.reorderList_deque(u)
        self.compare(u, o)


if __name__ == '__main__':
    unittest.main(verbosity=2)