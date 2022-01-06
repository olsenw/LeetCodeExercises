# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    There is a car with capacity empty seats. The vehicle only drives
    East (ie it cannot turn around and drive West).

    Given the capacity of the car and an array of trips where 
    trip[i] = [numPassenger_i, from_i, to_i] indicates that the ith trip
    has numPassangers and the locations to pick them up and drop them
    off are from and to respectively. The locations are given as the 
    number of kilometers due East from the car's initial location.

    Return true if it is possible to pick up and drop off all passengers
    for all the given trips, or false otherwise.

    Constraints
      1 <= len(trips) <= 1000
      len(trip[i]) == 3
      1 <= numPassangers <= 100
      0 <= from < to <= 1000          <-- (Important for O(n) solution)
      1 <= capacity <= 10^5
    '''
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        t = [0 for _ in range(1001)]
        for trip in trips:
            for i in range(trip[1], trip[2]):
                t[i] += trip[0]
                if t[i] > capacity:
                    return False
        return True

    '''
    idea based on leetcode discussion post
    https://leetcode.com/problems/car-pooling/discuss/1669547/Java-or-A-Simple-Solution
    
    similar to previous but only updating capacity at from, to positions
    (by adding at from and subtracting at to) and checking that sum over
    the whole array never exceeds capacity
    
    this saves the unneeded for loop checking/incrementing between from
    and to in previous solution.
    '''
    def carPooling_alt(self, trips: List[List[int]], capacity: int) -> bool:
        t = [0 for _ in range(1001)]
        for trip in trips:
            t[trip[1]] += trip[0]
            t[trip[2]] -= trip[0]
        s = 0
        for i in t:
            s += i
            if s > capacity:
                return False
        return True

    '''
    Other solutions exist, making use of sorting, priority queues, etc.
    These would have time of O(nlogn) due to the sort requirement, which
    is asymptotically worse the O(n) of above solutions.
    
    However performance wise this might be unlikely given the relatively
    small constraints in this problem. Would need to check with real
    timings. (rough check indicates O(n) is better here)
    
    These other solutions would be required if the max length of the
    trip was unknown.
    '''

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        c = 4
        i = [[2,1,5],[3,3,7]]
        o = False
        self.assertEqual(s.carPooling(i, c), o)
        self.assertEqual(s.carPooling_alt(i, c), o)

    def test_two(self):
        s = Solution()
        c = 5
        i = [[2,1,5],[3,3,7]]
        o = True
        self.assertEqual(s.carPooling(i, c), o)
        self.assertEqual(s.carPooling_alt(i, c), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)