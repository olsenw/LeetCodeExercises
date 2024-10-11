# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There is a party where n friends numbered from 0 to n - 1 are attending.
    There is an infinite number of chairs in this party that are numbered from 0
    to infinity. When a friend arrives at the party, they sit on the unoccupied
    chair with the smallest number.

    When a friend leaves the party, their chair becomes unoccupied at the moment
    they leave. If another friend arrives at that same moment, they can sit in
    that chair.

    Given a 0-indexed 2D integer array times where
    times[i] = [arrivali, leavingi], indicating the arrival and leaving times of
    the ith friend respectively, and an integer targetFriend. All arrival times
    are distinct.

    Return the chair number that the friend numbered targetFriend will sit on.
    '''
    # note that times is ordered by friend index...
    def smallestChair_misread_question(self, times: List[List[int]], targetFriend: int) -> int:
        answer = 0
        seats = list(range(len(times)))
        friends = []
        times.sort()
        for i,j in times:
            while friends and friends[0][0] <= i:
                heapq.heappush(seats, heapq.heappop(friends)[2])
            chair = heapq.heappop(seats)
            if answer == targetFriend:
                return chair
            else:
                answer += 1
                heapq.heappush(friends, (j,i,chair))
        return -1

    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        friends = sorted(range(len(times)), key=lambda x: times[x])
        chairs = list(range(len(times)))
        seats = []
        for i in friends:
            a,b = times[i]
            while seats and seats[0][0] <= a:
                heapq.heappush(chairs, heapq.heappop(seats)[2])
            chair = heapq.heappop(chairs)
            if i == targetFriend:
                return chair
            else:
                heapq.heappush(seats, (b,a,chair))
        return 0

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,4],[2,3],[4,6]], 1
        o = 1
        self.assertEqual(s.smallestChair(*i), o)

    def test_two(self):
        s = Solution()
        i = [[3,10],[1,5],[2,6]], 0
        o = 2
        self.assertEqual(s.smallestChair(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)