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
    Given the head of a singly linked list, return true if it is a
    palindrome or false otherwise.
    '''
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        '''
        brute = []
        while head:
            brute.append(head.val)
            head = head.next
        return all(a == b for a,b in zip(brute,reversed(brute)))
        '''
        '''
        dummy = None
        h = head
        while h:
            dummy = ListNode(h.val, dummy)
            h = h.next
        while head:
            if head.val != dummy.val:
                return False
            head = head.next
            dummy = dummy.next
        return True
        '''
        # O(n) time and O(1) space
        # find midpoint
        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        # reverse last half
        prev = None
        while slow:
            curr = slow.next
            slow.next = prev
            prev = slow
            slow = curr
        # compare
        while head and prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
        o = True
        self.assertEqual(s.isPalindrome(i), o)

    def test_two(self):
        s = Solution()
        i = ListNode(1, ListNode(2))
        o = False
        self.assertEqual(s.isPalindrome(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)