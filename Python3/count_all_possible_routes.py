# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of distinct positive integers locations where locations[i]
    represents the position of city i. Also given are the integers start,
    finish, and fuel representing the starting city, ending city, and the
    initial amount of fuel respectively.

    At each step, starting at city i, it is possible to pick any city j such
    that j != i and 0 <= j < locations.length and move to city j. Moving from
    city i to city j reduces the amount of fuel by
    abs(locations[i] - locations[j]).

    Notice that fuel cannot become negative at any point in time, and that a
    city may be visited more than once (including start and finish).

    Return the count of all possible routes from start to finish. Since the
    answer may be large return it modulo 10**9 + 7.
    '''
    # fails
    def countRoutes_bfs_tle(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        dp = [[0] * (fuel + 1) for _ in locations]
        dp[start][fuel] = 1
        q = deque([(start, fuel)])
        while q:
            i,f = q.popleft()
            # ??? finish locations is the sum of all other spots assuming fuel???
            for j in range(len(locations)):
                k = abs(locations[i] - locations[j])
                if i != j and k <= f:
                    dp[j][f - k] += 1
                    q.append((j, f - k))
        return sum(dp[finish]) % (10**9 + 7)

    # based on leetcode solution
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        m = 10**9 + 7
        @cache
        def dp(i, f):
            if f < 0:
                return 0
            answer = 1 if i == finish else 0
            for j in range(len(locations)):
                if i != j:
                    answer = (answer + dp(j, f - abs(locations[i] - locations[j]))) % m
            return answer
        return dp(start, fuel)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,3,6,8,4]
        j = 1
        k = 3
        l = 5
        o = 4
        self.assertEqual(s.countRoutes(i,j,k,l), o)
    
    def test_two(self):
        s = Solution()
        i = [4,3,1]
        j = 1
        k = 0
        l = 6
        o = 5
        self.assertEqual(s.countRoutes(i,j,k,l), o)
    
    def test_three(self):
        s = Solution()
        i = [1,2]
        j = 0
        k = 0
        l = 1
        o = 1
        self.assertEqual(s.countRoutes(i,j,k,l), o)
    
    def test_four(self):
        s = Solution()
        i = [1,2]
        j = 0
        k = 0
        l = 200
        o = 101
        self.assertEqual(s.countRoutes(i,j,k,l), o)
    
    def test_five(self):
        s = Solution()
        i = [1,2,3]
        j = 0
        k = 2
        l = 40
        o = 615088286
        self.assertEqual(s.countRoutes(i,j,k,l), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)