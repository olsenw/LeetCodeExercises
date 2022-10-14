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
    Given the head of a linked list delete the middle node, and return the head
    of the modified linked list.
    
    The middle node of a linked list of size n is the ⌊n / 2⌋th node from the
    start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than
    or equal to x.
    * ie n = 1,2,3,4,5 the middles nodes are 0,1,1,2,2
    '''
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        i, j, k = head, head, dummy
        while i.next and i.next.next:
            i = i.next.next
            k = j
            j = j.next
        if i.next:
            k = j
            j = j.next
        k.next = j.next
        del(j)
        return dummy.next

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,4,5]
        o = 5
        self.assertEqual(s.deleteMiddle(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,4,5]
        o = 5
        self.assertEqual(s.deleteMiddle(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)