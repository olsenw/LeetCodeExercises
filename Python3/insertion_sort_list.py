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
    def vals(self):
        if self and self.next:
            return str(self.val) + "," + self.next.vals()
        elif self:
            return str(self.val)
        else:
            return ""
    def __str__(self):
        return "[" + self.vals() + "]"

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        unsorted = head.next
        head.next = None
        while unsorted:
            # test if insert at begining (head) of sorted list
            if unsorted.val <= head.val:
                '''
                n = unsorted.next
                unsorted.next = sorted
                sorted = unsorted
                unsorted = n
                '''
                unsorted.next, head, unsorted = head, unsorted, unsorted.next
                continue
            # find where in list to insert
            insert = head
            while insert:
                if insert.next and unsorted.val <= insert.next.val:
                    break # found two node to insert between
                elif insert.next:
                    insert = insert.next # check next node
                else:
                    break # no more nodes, insert end of list
            unsorted.next, insert.next, unsorted = insert.next, unsorted, unsorted.next
        return head

class UnitTesting(unittest.TestCase):
    # actual test to run on Solution
    def test_one(self):
        s = Solution()
        t = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
        self.assertEqual(str(s.insertionSortList(t)), "[1,2,3,4]")

    def test_two(self):
        s = Solution()
        t = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))
        self.assertEqual(str(s.insertionSortList(t)), "[-1,0,3,4,5]")

if __name__ == '__main__':
    unittest.main(verbosity=2)