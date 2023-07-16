# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    For a project there is a list of required skills req_skills, and a list of
    people. The ith person people[i] contains a list of skills that the person
    has.

    Consider a sufficient team: a set of people such that for every required
    skill in req_skills, there is at least one person in the team who has that
    skill. The teams can be represented by the index of each person.

    Return any sufficient team of the smallest possible size, represented by the
    index of each person. The answer may be returned in any order.

    The test cases are designed such than an answer exists.
    '''
    # time limit exceeded (8 / 38 test cases)
    # right idea... but poor choice for dp states (to complex)
    def smallestSufficientTeam_tle(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        m = len(req_skills)
        n = len(people)
        # skill name -> to index in skill maps
        skill_map = {j:i for i,j in enumerate(req_skills)}
        target = 1
        for _ in range(m-1):
            target <<= 1
            target |= 1
        # person -> mask of skills possessed
        people_skills = {i:0 for i in range(n)}
        for i in range(n):
            for j in people[i]:
                people_skills[i] |= 1 << skill_map[j]
        # index of person be being considered, current team (mask)
        @cache
        def dp(index, team):
            mask = 0
            for i in range(n):
                j = 1 << i
                if j & team != 0:
                    mask |= people_skills[i]
            if mask == target:
                return team
            if index == n:
                return 0
            # add person to team
            a = dp(index + 1, team | 1 << index)
            # do not add person to team
            b = dp(index + 1, team)
            # return smallest team (with at least one person)
            x = bin(a)[2:].count('1')
            y = bin(b)[2:].count('1')
            if x > 0 and y > 0:
                if x > y:
                    return b
                else:
                    return a
            elif x > 0 or y > 0:
                if x > 0:
                    return a
                else:
                    return b
            else:
                return 0 
        answer = []
        team = dp(0,0)
        for i in range(n):
            j = 1 << i
            if j & team != 0:
                answer.append(i)
        return answer

    # based on leetcode solution
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        m = len(req_skills)
        n = len(people)
        skill_map = {j:i for i,j in enumerate(req_skills)}
        people_skills = {i:0 for i in range(n)}
        for i in range(n):
            for j in people[i]:
                people_skills[i] |= 1 << skill_map[j]
        dp = [2**n - 1] * (2**m)
        dp[0] = 0
        for skill_mask in range(1, 2**m):
            for i in range(n):
                missing_skills = skill_mask & ~people_skills[i]
                if missing_skills != skill_mask:
                    people_mask = dp[missing_skills] | 2**i
                    if people_mask.bit_count() < dp[skill_mask].bit_count():
                        dp[skill_mask] = people_mask
        answer = []
        for i in range(n):
            j = 1 << i
            if j & dp[2**m - 1] != 0:
                answer.append(i)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["java","nodejs","reactjs"]
        j = [["java"],["nodejs"],["nodejs","reactjs"]]
        o = [0,2]
        self.assertEqual(sorted(s.smallestSufficientTeam(i,j)), o)

    def test_two(self):
        s = Solution()
        i = ["algorithms","math","java","reactjs","csharp","aws"]
        j = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
        o = [1,2]
        self.assertEqual(sorted(s.smallestSufficientTeam(i,j)), o)

    # def test_three(self):
    #     s = Solution()
    #     i = ["hdbxcuzyzhliwv","uvwlzkmzgis","sdi","bztg","ylopoifzkacuwp","dzsgleocfpl"]
    #     j = [["hdbxcuzyzhliwv","dzsgleocfpl"],["hdbxcuzyzhliwv","sdi","ylopoifzkacuwp","dzsgleocfpl"],["bztg","ylopoifzkacuwp"],["bztg","dzsgleocfpl"],["hdbxcuzyzhliwv","bztg"],["dzsgleocfpl"],["uvwlzkmzgis"],["dzsgleocfpl"],["hdbxcuzyzhliwv"],[],["dzsgleocfpl"],["hdbxcuzyzhliwv"],[],["hdbxcuzyzhliwv","ylopoifzkacuwp"],["sdi"],["bztg","dzsgleocfpl"],["hdbxcuzyzhliwv","uvwlzkmzgis","sdi","bztg","ylopoifzkacuwp"],["hdbxcuzyzhliwv","sdi"],["hdbxcuzyzhliwv","ylopoifzkacuwp"],["sdi","bztg","ylopoifzkacuwp","dzsgleocfpl"],["dzsgleocfpl"],["sdi","ylopoifzkacuwp"],["hdbxcuzyzhliwv","uvwlzkmzgis","sdi"],[],[],["ylopoifzkacuwp"],[],["sdi","bztg"],["bztg","dzsgleocfpl"],["sdi","bztg"]]
    #     o = [0,2]
    #     self.assertEqual(sorted(s.smallestSufficientTeam(i,j)), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)