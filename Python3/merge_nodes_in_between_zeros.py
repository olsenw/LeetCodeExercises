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
    Given the head of a linked list, which contains a series of integers
    separated by 0's. The beginning and end of the linked list will have
    Node.val == 0.

    For every two consecutive 0's merge all the nodes lying between them into a
    single node whose value is the sum of all the merged nodes. The modified
    list should not contain any 0's.

    Return the head of the modified linked list.
    '''
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head.next
        head = ListNode()
        answer = head
        s = 0
        while curr:
            if curr.val == 0:
                answer.next = ListNode(s)
                answer = answer.next
                s = 0
            else:
                s += curr.val
            curr = curr.next
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