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
    Given the head of a singly linked list and an integer k, split the linked
    list into k consecutive linked list parts.

    The length of each part should be as equal as possible: no two parts should
    have a size differing by more than one. This may lead to some parts being
    null.

    The parts should be in the order of occurrence in the input list, and parts
    occurring earlier should always have a size greater than or equal to parts
    occurring later.

    Return an array of the k parts.
    '''
    # little cheap to convert to a python list first... could be converted to
    # actual ListNode instead
    # answer fundamentally agrees with the editorial
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        nodes = []
        while head:
            nodes.append(head.val)
            head = head.next
        n = len(nodes)
        count = n // k
        extra = n % k
        # print(nodes)
        # print(n,count,extra)
        answer = [ListNode(-1) for _ in range(k)]
        i = 0
        for a in range(k):
            target = i + count
            if extra:
                target += 1
                extra -= 1
            # print(i, target)
            curr = answer[a]
            while i < target:
                curr.next = ListNode(nodes[i])
                curr = curr.next
                i += 1
        return [a.next for a in answer]

class UnitTesting(unittest.TestCase):
    '''
    tested online
    '''
    pass

if __name__ == '__main__':
    unittest.main(verbosity=2)