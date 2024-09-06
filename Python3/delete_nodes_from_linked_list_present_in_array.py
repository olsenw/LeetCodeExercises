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
    Given an array of integers nums and the head of a linked list. Return the
    head of the modified linked list after removing all nodes from the linked
    list that have a value that exists in nums.
    '''
    # abuses memory
    def modifiedList_sucks(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        dummy = ListNode()
        fake = dummy
        curr = head
        while curr:
            if curr.val not in nums:
                fake.next = ListNode(curr.val)
                fake = fake.next
            curr = curr.next
        return dummy.next

    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        dummy = ListNode(0, head)
        curr = dummy
        while curr.next:
            if curr.next.val in nums:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next

class UnitTesting(unittest.TestCase):
    '''tested online cause of ListNode lazy'''
    pass

if __name__ == '__main__':
    unittest.main(verbosity=2)