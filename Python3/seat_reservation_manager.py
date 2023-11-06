# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

'''
Design a system that manages the reservation state of n seats that are numbered
from 1 to n.

Implement the SeatManager class:
'''
class SeatManager:
    '''
    Initializes a SeatManager object that will manage n seats numbered from 1 to
    n. All seats are initially available.
    '''
    def __init__(self, n: int):
        self.heap = [i for i in range(1, n + 1)]
        heapq.heapify(self.heap)

    '''
    Fetches the smallest-numbered unreserved seat, reserves it, and returns its
    number.
    '''
    def reserve(self) -> int:
        return heapq.heappop(self.heap)

    '''
    Unreserves the seat with the given seatNumber.
    '''
    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.heap, seatNumber)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = SeatManager(5)
        self.assertEqual(s.reserve(), 1)
        self.assertEqual(s.reserve(), 2)
        s.unreserve(2)
        self.assertEqual(s.reserve(), 2)
        self.assertEqual(s.reserve(), 3)
        self.assertEqual(s.reserve(), 4)
        self.assertEqual(s.reserve(), 5)
        s.unreserve(5)

if __name__ == '__main__':
    unittest.main(verbosity=2)