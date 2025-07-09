# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer eventTime denoting the duration of an event, where the
    event occurs from time t = 0 to time t = eventTime.

    Also given are two integer arrays startTime and endTime, each of length n.
    These represent the start and end time of n non-overlapping meetings, where
    the ith meeting occurs during the time [startTime[i], endTime[i]].

    It is possible to reschedule at most at most k meetings by moving their
    start time while maintaining the same duration, to maximize the longest
    continuous period of free time during the event.

    The relative order of all the meetings should stay the same and they should
    remain non-overlapping.

    Return the maximum amount of free time possible after rearranging the
    meetings.

    Note that the meetings can not be rescheduled to a time outside the event.
    '''
    # based on hints
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        startTime.append(eventTime)
        running = sum(endTime[i] - startTime[i] for i in range(k))
        left, right = 0, startTime[k]
        answer = right - left - running
        pass
        for i in range(k, n):
            running -= endTime[i-k] - startTime[i-k]
            running += endTime[i] - startTime[i]
            left = endTime[i - k]
            right = startTime[i+1]
            answer = max(answer, right - left - running)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 5
        j = 1
        k = [1,3]
        l = [2,5]
        o = 2
        self.assertEqual(s.maxFreeTime(i,j,k,l), o)

    def test_two(self):
        s = Solution()
        i = 10
        j = 1
        k = [0,2,9]
        l = [1,4,10]
        o = 6
        self.assertEqual(s.maxFreeTime(i,j,k,l), o)

    def test_three(self):
        s = Solution()
        i = 5
        j = 2
        k = [0,1,2,3,4]
        l = [1,2,3,4,5]
        o = 0
        self.assertEqual(s.maxFreeTime(i,j,k,l), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)