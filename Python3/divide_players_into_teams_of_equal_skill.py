# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a positive integer array skill of even length n where skill[i] denotes
    the skill of the ith player. Divide the players into n / 2 teams of 2 such
    that the total skill of each team is equal.

    The chemistry of a team is equal to the product of the skills of the players
    on that team.

    Return the sum of the chemistry of all the teams, or return -1 if there is
    noo way to divide the players into teams such that the total skill of each
    team is equal.
    '''
    # hints give it away
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        answer = 0
        t = skill[0] + skill[-1]
        for i in range(len(skill) // 2):
            if skill[i] + skill[-i-1] == t:
                answer += skill[i] * skill[-i-1]
            else:
                return -1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,2,5,1,3,4]
        o = 22
        self.assertEqual(s.dividePlayers(i), o)

    def test_two(self):
        s = Solution()
        i = [3,4]
        o = 12
        self.assertEqual(s.dividePlayers(i), o)

    def test_three(self):
        s = Solution()
        i = [1,1,2,3]
        o = -1
        self.assertEqual(s.dividePlayers(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)