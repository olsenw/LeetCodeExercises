# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    In a special ranking system, each voter gives a rank from highest to lowest
    to all teams participating in the competition.

    The ordering of teams is decided by who received the most position-one
    votes. If two or more teams tie in the first position, consider the second
    position to resolve the conflict, if they tie again, continue this process
    until the ties are resolved. If two or more teams are still tied after
    considering all positions, rank them alphabetically based on their team
    letter.

    Given an array of strings votes which is the votes of all voters in the
    ranking systems. Sort all teams according to the ranking system described
    above.

    Return a string of all teams sorted by the ranking system.
    '''
    def rankTeams_incomplete(self, votes: list[str]) -> str:
        m,n = len(votes[0]), len(votes)
        positions = [Counter()] * (m+1)
        for v in votes:
            for i,j in enumerate(v):
                positions[i][j] += 1
        for v in votes[0]:
            positions[-1][v] = ord(v)
        return

    def rankTeams(self, votes: list[str]) -> str:
        counts = {v:[0]*len(votes[0]) + [-ord(v)] for v in votes[0]}
        for v in votes:
            for i,j in enumerate(v):
                # j = ord(j) - ord('A')
                counts[j][i] += 1
        answer = ""
        def winner(teams:str, position:int) -> str:
            if len(teams) == 1:
                return teams
            m = max(counts[v][position] for v in teams)
            teams = "".join(v for v in teams if counts[v][position] == m)
            return winner(teams, position+1)
        for i in range(len(votes[0])):
            teams = "".join(v for v in votes[0] if v not in answer)
            answer += winner(teams, 0)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["ABC","ACB","ABC","ACB","ACB"]
        o = "ACB"
        self.assertEqual(s.rankTeams(i), o)

    def test_two(self):
        s = Solution()
        i = ["WXYZ","XYZW"]
        o = "XWYZ"
        self.assertEqual(s.rankTeams(i), o)

    def test_three(self):
        s = Solution()
        i = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]
        o = "ZMNAGUEDSJYLBOPHRQICWFXTVK"
        self.assertEqual(s.rankTeams(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)