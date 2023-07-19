# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of intervals intervals where intervals[i] = [starti, endi],
    return the minimum number of intervals that have to be removed to make the
    rest of the intervals non-overlapping.
    '''
    # fails (greedy based on start)
    def eraseOverlapIntervals_wrong(self, intervals: List[List[int]]) -> int:
        answer = 0
        # sort by start time
        intervals.sort(key=lambda x:(x[0],-x[1]))
        # intervals = sorted([j-i,i,j] for i,j in intervals)
        end = intervals[0][1]
        for i,j in intervals[1:]:
            if i < end:
                answer += 1
            else:
                end = j
        return answer

    # greedy base on end time
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by end time
        intervals.sort(key=lambda x: (x[1], x[0]))
        answer = 0
        end = intervals[0][1]
        for i,j in intervals[1:]:
            if i >= end:
                end = j
            else:
                answer += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,2],[2,3],[3,4],[1,3]]
        o = 1
        self.assertEqual(s.eraseOverlapIntervals(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,2],[1,2],[1,2]]
        o = 2
        self.assertEqual(s.eraseOverlapIntervals(i), o)

    def test_three(self):
        s = Solution()
        i = [[1,2],[2,3]]
        o = 0
        self.assertEqual(s.eraseOverlapIntervals(i), o)

    def test_four(self):
        s = Solution()
        i = [[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]
        o = 7
        self.assertEqual(s.eraseOverlapIntervals(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)