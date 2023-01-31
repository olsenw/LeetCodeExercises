# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from bisect import bisect_right
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    There is a manager for a basketball team. For the upcoming tournament, the
    manager wishes to choose the team with the highest overall score. The score
    of the team is the sum of scores of all the players in the team.

    However, the basketball team is not allowed to have conflicts. A conflict
    exists if a younger player has a strictly hight score than an older player.
    A conflict does not occur between players of the same age.

    Given two lists, scores and ages, where each score[i] and age[i] represents
    the score and age of the ith player, respectively, return the hightest
    overall score of all possible basketball teams.
    '''
    def bestTeamScore_incorrect(self, scores: List[int], ages: List[int]) -> int:
        n = len(ages)
        order = sorted(range(n), key=lambda x: ages[x])
        @cache
        def dp(i:int, s:int, a:int) -> int:
            if i == n:
                return 0
            p = order[i]
            # leave player order[i]
            x = dp(i + 1, s, a)
            # take player order[i]
            if a < ages[p] and scores[p] < s:
                y = 0
            else:
                y = scores[p] + dp(i + 1, max(s, scores[p]), max(a, ages[p]))
            return max(x,y)
        return dp(0,0,0)

    # based on top-down solution from leetcode
    # https://leetcode.com/problems/best-team-with-no-conflicts/solutions/2886659/best-team-with-no-conflicts/
    # was on right track... missed sort age AND score ascending
    # the condition of no previous (ie j starts at -1) also critical
    def bestTeamScore_tle(self, scores: List[int], ages: List[int]) -> int:
        n = len(ages)
        # sort young to old, lowest to highest score
        order = sorted(range(n), key=lambda x: (ages[x],scores[x]))
        @cache
        def dp(i:int, j:int) -> int:
            if i == n:
                return 0
            # leave = dp(i + 1, j)
            # take = 0
            # if j == -1 or scores[order[i]] >= scores[order[j]]:
            #     take = scores[order[i]] + dp(i + 1, i)
            # return max(leave, take)
            if j == -1 or scores[order[i]] >= scores[order[j]]:
                return max(dp(i+1,j), scores[order[i]] + dp(i + 1, i))
            return dp(i+1,j)
        return dp(0,-1)

    # solution by harshithdshetty
    # https://leetcode.com/problems/best-team-with-no-conflicts/solutions/3120715/python3-243-ms-faster-than-98-58-of-python3/?languageTags=python
    # dont know or care why it works and above does not
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        new_list = sorted(zip(ages, scores)) 
        visited = [new_list[0][1]] 
        dp = [new_list[0][1]] 
        ans = new_list[0][1] 

        for i in range(1,len(new_list)):
            s = new_list[i][1]
            index = bisect_right(visited, s) 
            curr = max(dp[:index]) + s if index else s 
            ans = max(ans, curr)
            visited.insert(index, s) 
            dp.insert(index,curr)
        return ans

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,3,5,10,15]
        j = [1,2,3,4,5]
        o = 34
        self.assertEqual(s.bestTeamScore(i,j), o)

    def test_two(self):
        s = Solution()
        i = [4,5,6,5]
        j = [2,1,2,1]
        o = 16
        self.assertEqual(s.bestTeamScore(i,j), o)

    def test_three(self):
        s = Solution()
        i = [1,2,3,5]
        j = [8,9,10,1]
        o = 6
        self.assertEqual(s.bestTeamScore(i,j), o)

    def test_four(self):
        s = Solution()
        i = [1,3,7,3,2,4,10,7,5]
        j = [4,5,2,1,1,2,4,1,4]
        o = 29
        self.assertEqual(s.bestTeamScore(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)