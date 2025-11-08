# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

'''
The RecentCounter class counts the number of recent requests within a certain
time frame.

Implement the RecentCounter class:
'''
class RecentCounter:
    '''
    Initializes the counter with zero recent requests.
    '''
    def __init__(self):
        self.heap = []
        return

    '''
    Adds a new request at time t, where t represents some time in milliseconds,
    and returns the number of requests that has happened in the past 3000
    milliseconds (including the new request). Specifically, return the number of
    requests that have happened in the inclusive range [t - 3000, t].

    It is guaranteed that every call to ping uses a strictly larger value of t
    than the previous call.
    '''
    def ping(self, t: int) -> int:
        while self.heap and self.heap[0] < t - 3000:
            heapq.heappop(self.heap)
        heapq.heappush(self.heap, t)
        return len(self.heap)

class UnitTesting(unittest.TestCase):

    def test_two(self):
        s = RecentCounter()
        self.assertEqual(s.ping(1), 1)
        self.assertEqual(s.ping(100), 2)
        self.assertEqual(s.ping(3001), 3)
        self.assertEqual(s.ping(3002), 3)

if __name__ == '__main__':
    unittest.main(verbosity=2)