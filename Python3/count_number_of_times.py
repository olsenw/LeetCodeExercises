# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There are n soldiers standing in a line. Each soldier is assigned a unique
    rating value.

    Form teams of 3 solders using the following rules:
    * Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j],
      rating[k]).
    * A team is valid if: (rating[i] < rating[j] rating[k]) or (rating[i] >
      rating[j] > rating[k]) where 0 <= i < j < k < n).

    Return the number of teams that can be formed given the conditions. Soldiers
    can be part of multiple teams.
    '''
    # brute force O(n^3)
    def numTeams_tle(self, rating: List[int]) -> int:
        n = len(rating)
        a = 0
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if rating[i] < rating[j] < rating[k]:
                        a += 1
                    if rating[i] > rating[j] > rating[k]:
                        a += 1
        return a

    # based on LeetCode editorial
    # https://leetcode.com/problems/count-number-of-teams/editorial/?envType=daily-question&envId=2024-07-29
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        @cache
        def increasing(index, team):
            if index == n:
                return 0
            if team == 3:
                return 1
            valid = 0
            for i in range(index + 1, n):
                if rating[i] > rating[index]:
                    valid += increasing(i, team + 1)
            return valid
        @cache
        def decreasing(index, team):
            if index == n:
                return 0
            if team == 3:
                return 1
            valid = 0
            for i in range(index + 1, n):
                if rating[i] < rating[index]:
                    valid += decreasing(i, team + 1)
            return valid
        answer = 0
        for i in range(n):
            answer += increasing(i, 1)
            answer += decreasing(i, 1)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,5,3,4,1]
        o = 3
        self.assertEqual(s.numTeams(i), o)

    def test_two(self):
        s = Solution()
        i = [2,1,3]
        o = 0
        self.assertEqual(s.numTeams(i), o)

    def test_three(self):
        s = Solution()
        i = [1,2,3,4]
        o = 4
        self.assertEqual(s.numTeams(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)