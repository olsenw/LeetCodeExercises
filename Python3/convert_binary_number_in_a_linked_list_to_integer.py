# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    '''
    Given the head of a singly-linked list containing the values of 0 or
    or 1 representing a binary number

    Return the decimal value of the binary number

    Constraints:
    List is not empty
    No more than 30 nodes
    Each node's value is either 0 or 1
    '''
    def getDecimalValue(self, head: ListNode) -> int:
        # stat with first node
        number = head.val
        # check if another node (ie can I work with it)
        while head.next:
            # left shift and bitwise or with next value
            number = number << 1 | head.next.val
            # advance list
            head = head.next
        return number

    '''
    # First attemp (note it does work)
    def getDecimalValue(self, head: ListNode) -> int:
        number = 0
        shift = lambda num, val: (num << 1) ^ val
        while head.next is not None:
            # print(head.val, end=" ")
            number = shift(number, head.val)
            head = head.next
        else:
            number = shift(number, head.val)
            # print(head.val, " = ", number)
        return number
    '''

class UnitTesting(unittest.TestCase):
    # actual test to run on Solution
    def test_one(self):
        s = Solution()
        l = ListNode(1, ListNode(0, ListNode(1)))
        self.assertEqual(s.getDecimalValue(l), 5)

    def test_two(self):
        s = Solution()
        l = ListNode(0)
        self.assertEqual(s.getDecimalValue(l), 0)

    def test_three(self):
        s = Solution()
        l = ListNode(1)
        self.assertEqual(s.getDecimalValue(l), 1)

    def test_four(self):
        s = Solution()
        l = ListNode(1, ListNode(0, ListNode(0, ListNode(1, ListNode(0, ListNode(0, ListNode(1, ListNode(1, ListNode(1, ListNode(0, ListNode(0, ListNode(0, ListNode(0, ListNode(0, ListNode(0)))))))))))))))
        self.assertEqual(s.getDecimalValue(l), 18880)

    def test_five(self):
        s = Solution()
        l = ListNode(0, ListNode(0))
        self.assertEqual(s.getDecimalValue(l), 0)

if __name__ == '__main__':
    unittest.main(verbosity=2)