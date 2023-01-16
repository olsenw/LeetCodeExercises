# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    # logic issue
    def insert_fails(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        answer = []
        i = 0
        x,y = newInterval
        # append intervals to answer until overlap is detected
        while i < len(intervals):
            a,b = intervals[i]
            if b < x:
                answer.append([a,b])
            else:
                break
            i += 1
        # merge overlap
        s, e = min(a, x), max(b, y)
        while i < len(intervals) and a <= e:
            s, e = min(a, s), max(b, e)
            a,b = intervals[i]
            i += 1
        pass
        answer.append([s,e])
        # collect remaining intervals
        while i < len(intervals):
            answer.append(intervals[i])
            i += 1
        return answer

    def insert_fails_again(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Empty list
        if not len(intervals):
            return [newInterval]
        # Insert at start of list
        if newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals
        # Insert at end of list
        if intervals[-1][1] < newInterval[0]:
            return intervals + [newInterval]
        # Find insert position
        answer = []
        i,j = 0, len(intervals) - 1
        x,y = newInterval
        while i < len(intervals):
            a,b = intervals[i]
            if (a <= x <= b <= y) or (x <= a <= y <= b) or (a <= x <= y <= b) or (x <= a <= b <= y):
                break
            i += 1
        while j > 0:
            a,b = intervals[j]
            if (a <= x <= b <= y) or (x <= a <= y <= b) or (a <= x <= y <= b) or (x <= a <= b <= y):
                break
            j -= 1
        # no overlap detected
        if j < i:
            k = 0
            while k < len(intervals) - 1:
                k += 1
        x,y = min(intervals[i][0], x), max(intervals[j][1], y)
        return intervals[0:i] + [[x,y]] + intervals[j+1:len(intervals)]

    # solution by DebbieAlter
    # https://leetcode.com/problems/insert-interval/solutions/844549/python-super-short-simple-clean-solution-99-faster/?orderBy=most_votes&languageTags=python3
    # linear search (what trying to do but smarter)
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        
        for interval in intervals:
			# the new interval is after the range of other interval, so we can leave the current interval baecause the new one does not overlap with it
            if interval[1] < newInterval[0]:
                result.append(interval)
            # the new interval's range is before the other, so we can add the new interval and update it to the current one
            elif interval[0] > newInterval[1]:
                result.append(newInterval)
                newInterval = interval
            # the new interval is in the range of the other interval, we have an overlap, so we must choose the min for start and max for end of interval 
            elif interval[1] >= newInterval[0] or interval[0] <= newInterval[1]:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        
        result.append(newInterval); 
        return result

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,3],[6,9]]
        j = [2,5]
        o = [[1,5],[6,9]]
        self.assertEqual(s.insert(i,j), o)

    def test_two(self):
        s = Solution()
        i = [[1,2],[3,5],[6,7],[8,10],[12,16]]
        j = [4,8]
        o = [[1,2],[3,10],[12,16]]
        self.assertEqual(s.insert(i,j), o)

    def test_three(self):
        s = Solution()
        i = []
        j = [4,8]
        o = [[4,8]]
        self.assertEqual(s.insert(i,j), o)

    def test_four(self):
        s = Solution()
        i = [[1,5]]
        j = [4,8]
        o = [[1,8]]
        self.assertEqual(s.insert(i,j), o)

    def test_five(self):
        s = Solution()
        i = [[1,5]]
        j = [0,6]
        o = [[0,6]]
        self.assertEqual(s.insert(i,j), o)

    def test_six(self):
        s = Solution()
        i = [[1,5],[6,8]]
        j = [0,9]
        o = [[0,9]]
        self.assertEqual(s.insert(i,j), o)

    def test_seven(self):
        s = Solution()
        i = [[3,5],[12,15]]
        j = [6,6]
        o = [[3,5],[6,6],[12,15]]
        self.assertEqual(s.insert(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)