# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

from sortedcontainers import SortedSet

'''
There is an exam room with n seats in a single row labeled from 0 to n - 1.

When a student enters the room, they must sit in the seat that maximizes the
distance to the closest person. If there are multiple such seats, they sit in
the seat with the lowest number. If no one is in the room, then the students
sits at seat number 0.

Design a class that simulates the mentioned exam room.
'''
# derived from solution by subtlecold
# https://leetcode.com/problems/exam-room/solutions/2414385/python-o-logn-both-seat-and-leave-easier-to-understand/
class ExamRoom:
    '''
    Initializes the object of the exam room with the number of the seats n.
    '''
    def __init__(self, n: int):
        self.n = n
        # dict to hold neighbors
        self.seats = {}
        # heap of ranges
        self.heap = [(self.distance(-1, n), -1, n)]
    
    def distance(self, l, r):
        # leftmost seat is available to sit in
        if l == -1:
            return -r
        # rightmost seat is available to sit in
        elif r == self.n:
            return -(self.n - 1 - l)
        # sit in the middle of the range
        else:
            return -((r-l) // 2)
    '''
    Returns the label of the sea at which the next student will set.
    '''
    def seat(self) -> int:
        while self.heap:
            _, left, right = heapq.heappop(self.heap)
            # lazy delete the heap if the seat is already cleared
            if (left != -1 and (left not in self.seats or self.seats[left][1] != right)) \
               or (right != self.n and (right not in self.seats or self.seats[right][0] != left)):
                continue
            # assign seat 0 as it is available
            if left == -1:
                self.seats[0] = [-1, right]
                if right < self.n:
                    self.seats[right][0] = 0
                heapq.heappush(self.heap, (self.distance(0, right), 0, right))
                return 0
            # assign the last seat in the row
            elif right == self.n:
                self.seats[self.n - 1] = [left, self.n]
                self.seats[left][1] = self.n - 1
                heapq.heappush(self.heap, (self.distance(left, self.n - 1), left, self.n - 1))
                return self.n - 1
            # assign the middle seat between two people
            else:
                pos = (left + right) // 2
                self.seats[left][1] = pos
                self.seats[right][0] = pos
                self.seats[pos] = [left, right]
                heapq.heappush(self.heap, (self.distance(left, pos), left, pos))
                heapq.heappush(self.heap, (self.distance(pos, right), pos, right))
                return pos
        
    '''
    Indicates that the student sitting at seat p will leave the room. It is
    guaranteed that there will be a student sitting at seat p.
    '''
    def leave(self, p: int) -> None:
        left, right = self.seats[p]
        # update the left neighbor of seat to the right neighbor
        if left > -1:
            self.seats[left][1] = right
        # update the right neighbor of seat to the left neighbor
        if right < self.n:
            self.seats[right][0] = left
        # update the ranges heap with new range based on removed seats neighbors
        heapq.heappush(self.heap, (self.distance(left, right), left, right))
        # remove the seat (nobody is sitting in it)
        del self.seats[p]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = ExamRoom(10)
        self.assertEqual(s.seat(), 0)
        self.assertEqual(s.seat(), 9)
        self.assertEqual(s.seat(), 4)
        self.assertEqual(s.seat(), 2)
        s.leave(4)
        self.assertEqual(s.seat(), 5)

if __name__ == '__main__':
    unittest.main(verbosity=2)