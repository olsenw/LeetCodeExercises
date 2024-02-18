# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given n rooms numbered from 0 to n - 1.

    Also given a 2D integer array meetings where meetings[i] = [starti, endi]
    means that a meeting will be hel during the half-closed time interval
    [starti, endi). All the values of starti are unique.

    Meetings are allocated to rooms in the following manner:
    1) Each meeting will take place in the unused room with the lowest number.
    2) If there are no available rooms, the meeting will be delayed until a room
       becomes free. The delayed meeting should have the same duration as the
       original meeting.
    3) When a room becomes unused, meetings that have an earlier original start
       time should be given the room.
    
    Return the number of the room that held the most meetings. If there are
    multiple rooms, return the room with the lowest number.

    A half-closed interval [a,n) is the interval between a and b including a but
    not including b.
    '''
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        rooms = [0] * n
        available = [0] * n
        queue = deque(sorted(meetings))
        while queue:
            start, end = queue.popleft()
            pass
            for i in range(n):
                if available[i] <= start:
                    rooms[i] += 1
                    available[i] = end
                    break
            else:
                m = min(available)
                queue.appendleft([m, m + end - start])
        answer, meetings = 0, 0
        for i in range(n):
            if rooms[i] > meetings:
                answer = i
                meetings = rooms[i]
        return answer
    
    '''
    could do better if added a heap to track free rooms
    '''

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 2
        j = [[0,10],[1,5],[2,7],[3,4]]
        o = 0
        self.assertEqual(s.mostBooked(i,j), o)

    def test_two(self):
        s = Solution()
        i = 3
        j = [[1,20],[2,10],[3,5],[4,9],[6,8]]
        o = 1
        self.assertEqual(s.mostBooked(i,j), o)

    def test_three(self):
        s = Solution()
        i = 4
        j = [[18,19],[3,12],[17,19],[2,13],[7,10]]
        o = 0
        self.assertEqual(s.mostBooked(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)