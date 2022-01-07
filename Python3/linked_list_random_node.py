# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Optional

# needed for random numbers
import random

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def length(self) -> [int]:
        l = 0
        n = self
        while n:
            l += 1
            n = n.next
        return l

    def values(self) -> [int]:
        v = []
        n = self
        while n:
            v.append(n.val)
            n = n.next
        return v

'''
Given a singly linked list, return a random node's value from the linked
list. Each node must have the same probability of being chosen.
'''

# Really horrible solution... lots of iteration on list of unknown length
class SolutionOne:
    # O(n) time have to iterate list
    # O(1) space
    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.length = 0
        while head:
            self.length += 1
            head = head.next

    # O(n) potentially iterate list
    # O(1) space
    def getRandom(self) -> int:
        r = random.randrange(0,self.length)
        n = self.head
        while r > 0:
            n = n.next
            r -= 1
        return n.val

# really not much better, makes use of dictionary to limit getRandom iteration
class SolutionTwo:
    # how much to partition the quick access dictionary
    # ie max nodes increment through
    # impacts space needed
    partition = 2
    
    # O(n) time have to iterate the whole list
    # O(n/partition) space for lookup dictionary
    def __init__(self, head: Optional[ListNode]):
        self.length = 0
        self.spots = dict()
        while head:
            if self.length % self.partition == 0:
                self.spots[self.length] = head
            self.length += 1
            head = head.next

    # O(partition) time partition is max possible iterations
    # O(1) space
    def getRandom(self) -> int:
        r = random.randrange(0,self.length)
        div = (r // self.partition) * self.partition
        rem = r % self.partition
        n = self.spots[div]
        while rem > 0:
            n = n.next
            rem -= 1
        return n.val

'''
An alternative solution using reservoir sampling.
https://en.wikipedia.org/wiki/Reservoir_sampling

This code is pulled from the leetcode solution.
https://leetcode.com/problems/linked-list-random-node/solution/
'''
class SolutionReservoir:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        scope = 1
        chosen_value = 0
        curr = self.head

        while curr:
            # decide whether to include the element in reservoir
            if random.random() < 1 / scope:
                chosen_value = curr.val
            # move on to the next node
            curr = curr.next
            scope += 1
        return chosen_value

class UnitTesting(unittest.TestCase):
    def __helper(self, head, solution, test=1000):
        s = solution(head)
        if solution != SolutionReservoir:
            self.assertEqual(s.length, head.length())
        values = head.values()
        d = dict()
        dup = dict()
        for v in values:
            if v not in d:
                d[v] = 0
                dup[v] = 1
            else:
                dup[v] += 1
        # print(d)
        tests = 1000
        self.assertGreater(tests,100)
        for _ in range(tests):
            d[s.getRandom()] += 1
        # print(d)
        for i in d:
            d[i] //= dup[i]
            d[i] //= tests // 100
        # print(d)
        # print(dup)
        # print(min(d.values()), max(d.values()))
        self.assertAlmostEqual(min(d.values()), max(d.values()), delta=tests//100)

    '''
    tests for SolutionOne class
    '''
    def test_SolutionOne_one(self):
        random.seed(12345)
        l = ListNode(1, ListNode(2, ListNode(3)))
        self.__helper(l, SolutionOne)

    def test_SolutionOne_two(self):
        random.seed(12345)
        l = ListNode(2, ListNode(3, ListNode(1)))
        self.__helper(l, SolutionOne)

    def test_SolutionOne_three(self):
        random.seed(12345)
        l = ListNode(1, ListNode(1, ListNode(1)))
        self.__helper(l, SolutionOne)

    def test_SolutionOne_four(self):
        random.seed(12345)
        l = ListNode(2, ListNode(1, ListNode(1)))
        self.__helper(l, SolutionOne)

    def test_SolutionOne_five(self):
        random.seed(12345)
        l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(1))))))
        self.__helper(l, SolutionOne)

    '''
    tests for SolutionTwo class
    '''
    def test_SolutionTwo_one(self):
        random.seed(12345)
        l = ListNode(1, ListNode(2, ListNode(3)))
        self.__helper(l, SolutionTwo)

    def test_SolutionTwo_two(self):
        random.seed(12345)
        l = ListNode(2, ListNode(3, ListNode(1)))
        self.__helper(l, SolutionTwo)

    def test_SolutionTwo_three(self):
        random.seed(12345)
        l = ListNode(1, ListNode(1, ListNode(1)))
        self.__helper(l, SolutionTwo)

    def test_SolutionTwo_four(self):
        random.seed(12345)
        l = ListNode(2, ListNode(1, ListNode(1)))
        self.__helper(l, SolutionTwo)

    def test_SolutionTwo_five(self):
        random.seed(12345)
        l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(1))))))
        self.__helper(l, SolutionTwo)
        
    '''
    tests for SolutionReservoir class
    '''
    def test_SolutionReservoir_one(self):
        random.seed(12345)
        l = ListNode(1, ListNode(2, ListNode(3)))
        self.__helper(l, SolutionReservoir)

    def test_SolutionReservoir_two(self):
        random.seed(12345)
        l = ListNode(2, ListNode(3, ListNode(1)))
        self.__helper(l, SolutionReservoir)

    def test_SolutionReservoir_three(self):
        random.seed(12345)
        l = ListNode(1, ListNode(1, ListNode(1)))
        self.__helper(l, SolutionReservoir)

    def test_SolutionReservoir_four(self):
        random.seed(12345)
        l = ListNode(2, ListNode(1, ListNode(1)))
        self.__helper(l, SolutionReservoir)

    def test_SolutionReservoir_five(self):
        random.seed(12345)
        l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(1))))))
        self.__helper(l, SolutionReservoir)

if __name__ == '__main__':
    unittest.main(verbosity=2)