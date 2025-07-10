# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

from sortedcontainers import SortedDict, SortedList

class Solution:
    '''
    Given an integer eventTime denoting the duration of an event. Also give two
    integer arrays startTime and endTime, each of length n.

    These represent the start and end times of n non-overlapping meetings that
    occur during the event between time t = 0 and time t = eventTime, where the
    ith meeting occurs during the time [startTime[i], endTime[i]].

    It is possible to reschedule at most one meeting by moving its start time
    while maintaining the same duration, such that the meetings remain
    non-overlapping, to maximize the longest continuous period of free time
    during the event.

    Return the maximum amount of free time possible after rearranging the
    meetings.

    Note that the meetings can not be rescheduled to a time outside the event
    and they should remain non-overlapping.

    Note in this version, it is valid for the relative ordering of the meetings
    to change after rescheduling one meeting.
    '''
    def maxFreeTime_fails(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        startTime.append(eventTime)
        endTime = [0] + endTime
        n = len(startTime)
        answer = 0
        left = SortedList()
        right = SortedDict()
        for i in range(1, n-1):
            t = startTime[i] - endTime[i]
            if t in right:
                right[t] += 1
            else:
                right[t] = 1
        pass
        for i in range(1,n):
            size = endTime[i] - startTime[i-1]
            l = left.bisect_left(size)
            if l < len(left) and left[l] >= size:
                answer = max(answer, startTime[i + 1] - endTime[i - 1])
            r = right.bisect_left(size)
            if r < len(right) and right[right.keys()[r]] >= size:
                answer = max(answer, startTime[i + 1] - endTime[i - 1])
            left.add(startTime[i] + endTime[i-1])
            if right[startTime[i+1] - endTime[i]] > 1:
                right[startTime[i+1] - endTime[i]] -= 1
            else:
                right.pop(startTime[i+1] - endTime[i])
        return answer

    # based on LeetCode editorial
    # https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii/editorial/?envType=daily-question&envId=2025-07-10
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        # if meeting i can be moved
        movable = [False] * n
        # check if meeting can be moved left
        time = 0
        for i in range(n):
            if endTime[i] - startTime[i] <= time:
                movable[i] = True
            time = max(time, startTime[i] - (0 if i == 0 else endTime[i-1]))
        # check if meeting can be moved right
        time = 0
        for i in range(n-1, -1, -1):
            if endTime[i] - startTime[i] <= time:
                movable[i] = True
            time = max(time, (eventTime if i == n-1 else startTime[i+1]) - endTime[i])
        # find largest possible gap
        answer = 0
        for i in range(n):
            left = 0 if i == 0 else endTime[i-1]
            right = eventTime if i == n-1 else startTime[i+1]
            # possible to move meeting into another gap
            if movable[i]:
                answer = max(answer, right - left)
            # combine gaps on either side of meeting
            else:
                answer = max(answer, right - left - (endTime[i] - startTime[i]))
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 5
        j = [1,3]
        k = [2,5]
        o = 2
        self.assertEqual(s.maxFreeTime(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = 10
        j = [0,7,9]
        k = [1,8,10]
        o = 7
        self.assertEqual(s.maxFreeTime(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = 10
        j = [0,3,7,9]
        k = [1,4,8,10]
        o = 6
        self.assertEqual(s.maxFreeTime(i,j,k), o)

    def test_four(self):
        s = Solution()
        i = 5
        j = [0,1,2,3,4]
        k = [1,2,3,4,5]
        o = 0
        self.assertEqual(s.maxFreeTime(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)