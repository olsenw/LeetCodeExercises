# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two integer arrays, skill and mana, of length n and m, respectively.

    In a laboratory, n wizards must brew m potions in order. Each potion has a
    mana capacity mana[j] and must pass through all the wizards sequentially to
    be brewed properly. The time taken by the ith wizard on the jth potion is
    timeij = skill[i] * mana[j].

    Since the brewing process is delicate, a potion must be passed to the next
    wizard immediately after the current wizard completes their work. This means
    the timing must be synchronized so that each wizard begins working on a
    potion exactly when it arrives.

    Return the minimum amount of time required for the potions to be brewed
    properly.
    '''
    # derived from hints
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        # number of wizards with various skill levels
        n = len(skill)
        # number of potions to be brewed in order
        m = len(mana)
        # earliest moment a wizard is free
        free = [0] * len(skill)
        # iterate through the potions in order
        for p in range(m):
            # get the earliest time wizard 0 is free
            now = free[0]
            # calculate time it takes to run though the pipeline
            for w in range(1,n):
                now = max(now + skill[w-1] * mana[p], free[w])
            # reverse calculate when wizards are free
            free[n-1] = now + skill[n-1] * mana[p]
            for w in range(n-2,-1,-1):
                free[w] = free[w+1] - skill[w+1] * mana[p]
        return free[-1]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,5,2,4]
        j = [5,1,4,2]
        o = 110
        self.assertEqual(s.minTime(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,1,1]
        j = [1,1,1]
        o = 5
        self.assertEqual(s.minTime(i,j), o)

    def test_three(self):
        s = Solution()
        i = [1,2,3,4]
        j = [1,2]
        o = 21
        self.assertEqual(s.minTime(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)