# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import bisect
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 2D integer array intervals, where intervals[i] = [li, ri, weighti].
    Interval i starts at position li and ends at ri, and has a weight of
    weighti. Choose up to 4 non-overlapping intervals. The score of the chosen
    intervals is defined as the total sum of their weights.

    Return the lexicographically smallest array of at most 4 indices from
    intervals with maximum score, representing the choice of non-overlapping
    intervals.

    Two intervals are said to be non-overlapping if they do not share any
    points. In particular, intervals sharing a left or right boundary are 
    considered overlapping.
    '''
    # Based on Leetcode editorial
    # https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/editorial/?envType=daily-question&envId=2026-09-12
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        intervals = [(j,i,k,x) for x,(i,j,k) in enumerate(intervals)]
        intervals.sort(key=lambda x:x[0])
        dp = [[0] * 5 for _ in range(n+1)]
        indices = [[[] for _ in range(5)] for _ in range(n+1)]
        for i in range(n):
            right, left, weight, idx = intervals[i]
            # binary search to find intervals with right endpoints less than left
            t = bisect.bisect_left(intervals, (left,), hi=i)
            for j in range(1,5):
                s1 = dp[i][j]
                s2 = dp[t][j-1] + weight
                if s1 > s2:
                    dp[i+1][j] = dp[i][j]
                    indices[i+1][j] = indices[i][j].copy()
                    continue
                index = indices[t][j-1].copy()
                index.append(idx)
                index.sort()
                if s1 == s2 and indices[i][j] < index:
                    index = indices[i][j].copy()
                dp[i+1][j] = s2
                indices[i+1][j] = index
        return indices[i+1][j]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,3,2],[4,5,2],[1,5,5],[6,9,3],[6,7,1],[8,9,1]]
        o = [2,3]
        self.assertEqual(s.maximumWeight(i), o)

    def test_two(self):
        s = Solution()
        i = [[5,8,1],[6,7,7],[4,7,3],[9,10,6],[7,8,2],[11,14,3],[3,5,5]]
        o = [1,3,5,6]
        self.assertEqual(s.maximumWeight(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)