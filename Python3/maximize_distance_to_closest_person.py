# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an array representing a row of seats where seats[i]=1 
    represents a person sitting at the ith seat and seats[i]=0
    represents that the ith seat is empty. Note that the array is zero
    indexed.

    There is at least one empty seat, and at least one person sitting.

    A person wants to sit in the seat such that the distance between 
    them and the next closest person to them is maximized.

    Return the maximum distance between to the closest person.
    '''
    def maxDistToClosest(self, seats: List[int]) -> int:
        people = {i for i in range(len(seats)) if seats[i] == 1}
        d = 0
        while people:
            update = set()
            d += 1
            for p in people:
                if p-d >= 0 and seats[p-d] == 0:
                    seats[p-d] = 1
                    update.add(p)
                if p+d < len(seats) and seats[p+d] == 0:
                    seats[p+d] = 1
                    update.add(p)
            people = update
        return d-1

    def maxDistToClosest_2(self, seats: List[int]) -> int:
        from collections import deque
        people = deque()
        for i in range(len(seats)):
            if seats[i]:
                people.append(i)
        people.append(-1)
        d = 1
        while people:
            p = people.popleft()
            if p < 0:
                d += 1
                if people:
                    people.append(-1)
                continue
            add = False
            if p-d >= 0 and seats[p-d] == 0:
                seats[p-d] = 1
                add = True
            if p+d < len(seats) and seats[p+d] == 0:
                seats[p+d] = 1
                add = True
            if add:
                people.append(p)
        return d - 2

    def maxDistToClosest_3(self, seats: List[int]) -> int:
        i = 0
        d = 0
        distance = 1
        # left case (ie only person sitting to the right)
        while i < len(seats) and seats[i] == 0:
            d += 1
            i += 1
        distance = max(distance,d)
        # middle case (person left and right)
        d = 1
        for i in range(i, len(seats)):
            if i+1 < len(seats) and seats[i+1] == 1:
                distance = max(distance, d // 2)
                d = 1
            else:
                d += 1
        # right case (persons to the left)
        if i+1 == len(seats):
            distance = max(distance,d-2)

        return distance

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,0,0,0,1,0,1]
        o = 2
        self.assertEqual(s.maxDistToClosest(list(i)), o)
        self.assertEqual(s.maxDistToClosest_2(list(i)), o)
        self.assertEqual(s.maxDistToClosest_3(list(i)), o)

    def test_two(self):
        s = Solution()
        i = [1,0,0,0]
        o = 3
        self.assertEqual(s.maxDistToClosest(list(i)), o)
        self.assertEqual(s.maxDistToClosest_2(list(i)), o)
        self.assertEqual(s.maxDistToClosest_3(list(i)), o)

    def test_three(self):
        s = Solution()
        i = [0,1]
        o = 1
        self.assertEqual(s.maxDistToClosest(list(i)), o)
        self.assertEqual(s.maxDistToClosest_2(list(i)), o)
        self.assertEqual(s.maxDistToClosest_3(list(i)), o)

    def test_four(self):
        s = Solution()
        i = [0,0,1]
        o = 2
        self.assertEqual(s.maxDistToClosest(list(i)), o)
        self.assertEqual(s.maxDistToClosest_2(list(i)), o)
        self.assertEqual(s.maxDistToClosest_3(list(i)), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)