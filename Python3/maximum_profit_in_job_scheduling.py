# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from bisect import bisect_left
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    There are n jobs, where every job is scheduled to be done from startTime[i]
    to endTime[i], obtaining a profit of profit[i].

    Given the startTime, endTime and profit arrays, return the maximum profit
    that can be obtained given the condition that no two jobs in the subset have
    overlapping time ranges.

    If a job ends at time X is is possible to start another job at time X.
    '''
    # time limit exceeded (22/30 test cases passed)
    def jobScheduling_tle(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(profit)
        # indices of the three arrays sorted by start time
        indices = [i for i in range(n)]
        indices = sorted(indices, key=lambda x: (startTime[x],endTime[x]))
        @cache
        def dp(index,time):
            # ran out of jobs to consider
            if index == n:
                return 0
            # impossible to take this job
            if startTime[indices[index]] < time:
                return dp(index+1,time)
            # consider taking this job vs leaving this job
            a = profit[indices[index]] + dp(index+1,endTime[indices[index]])
            b = dp(index+1,time)
            return max(a,b)
        return dp(0,0)

    # needed a little help to find the bugs...
    # was correct other than indexing indices twice in the lambda
    # another issue was index needed to be >= n instead of == n
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(profit)
        # indices of the three arrays sorted by start time
        indices = [i for i in range(n)]
        indices = sorted(indices, key=lambda x: (startTime[x],endTime[x],profit[x]))
        @cache
        def dp(index):
            # ran out of jobs to consider
            if index >= n:
                return 0
            # take job
            i = bisect_left(indices,endTime[indices[index]],key=lambda x: startTime[x])
            a = profit[indices[index]] + dp(i)
            # leave the job
            b = dp(index+1)
            return max(a, b)
        return dp(0)

    # based on leetcode discussion post by stanislav-iablokov
    # https://leetcode.com/problems/maximum-profit-in-job-scheduling/discuss/2848695/PythonC%2B%2BRust-concise-DP-and-DFS-for-01-Knapsack-(explained)
    def jobScheduling_leetcode(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        
        @cache
        def dfs(i):
            if i >= len(jobs) : return 0
            k = bisect_left(jobs, jobs[i][1], key = lambda j: j[0])
            return max(dfs(i+1), jobs[i][2] + dfs(k))
            
        return dfs(0)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,3]
        j = [3,4,5,6]
        k = [50,10,40,70]
        o = 120
        self.assertEqual(s.jobScheduling(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,4,6]
        j = [3,5,10,6,9]
        k = [20,20,100,70,60]
        o = 150
        self.assertEqual(s.jobScheduling(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = [1,1,1]
        j = [2,3,4]
        k = [5,6,4]
        o = 6
        self.assertEqual(s.jobScheduling(i,j,k), o)

    def test_four(self):
        s = Solution()
        i = [4,2,4,8,2]
        j = [5,5,5,10,8]
        k = [1,2,8,10,4]
        o = 18
        self.assertEqual(s.jobScheduling(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)