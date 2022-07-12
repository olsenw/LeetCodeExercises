# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

from functools import cache

class Solution:
    '''
    Given an integer array matchsticks where matchsticks[i] is the
    length of the ith matchstick. All matchsticks should be used to make
    a single square. It is not possible to break a matchstick, but it is
    possible to link them up. Each matchstick must be used exactly one
    time.

    Return true if it is possible to make a square of the provided
    matchsticks, false otherwise.
    '''
    # timeout (incorrect see test case 6: [2,2,2,2,2,2] -> false)
    # for loop for(j) is incorrect allows numbers to be missed
    def makesquare_incorrect_timeout(self, matchsticks: List[int]) -> bool:
        sides = [0,0,0,0]
        def r(i):
            if i == len(matchsticks):
                return all(sides[0] == s for s in sides)
            for j in range(i, len(matchsticks)):
                for s in range(len(sides)):
                    sides[s] += matchsticks[j]
                    if r(j+1): return True
                    sides[s] -= matchsticks[j]
            return False
        return r(0)

    # 10/195 test cases
    def makesquare_timeout(self, matchsticks: List[int]) -> bool:
        @cache
        def r(i,a,b,c,d):
            if i == len(matchsticks):
                return a == b == c == d
            m = matchsticks[i]
            if r(i+1,a+m,b,c,d): return True
            if r(i+1,a,b+m,c,d): return True
            if r(i+1,a,b,c+m,d): return True
            if r(i+1,a,b,c,d+m): return True
            return False
        return r(0,0,0,0,0)

    # needed to read through leetcode solution dfs to make this work
    # O(4^n) time [four choices each stick]
    # O(n) space [recursive call stack]
    # same basic idea as above with additional checks to allow for early
    # returns. (side test, reverse sort, only recurse if side possible)
    def makesquare_dfs(self, matchsticks: List[int]) -> bool:
        # check if it is possible to make square
        side = sum(matchsticks)
        if side % 4:
            return False
        side //= 4
        # sort to get big sides out of way (performance boost)
        matchsticks.sort(reverse=True)
        def r(i,a,b,c,d):
            if i == len(matchsticks):
                return a == b == c == d
            m = matchsticks[i]
            if a+m <= side and r(i+1,a+m,b,c,d): return True
            if b+m <= side and r(i+1,a,b+m,c,d): return True
            if c+m <= side and r(i+1,a,b,c+m,d): return True
            if d+m <= side and r(i+1,a,b,c,d+m): return True
            return False
        return r(0,0,0,0,0)

    # based on dynamic programming leetcode solution
    # O(N * 2^N) time [iterate n times for 2^n possible masks]
    # O(N + 2^N) space [n for stack and 4 * 2^n for dp table]
    def makesquare(self, matchsticks: List[int]) -> bool:
        # check if it is possible to make square
        side = sum(matchsticks)
        if side % 4:
            return False
        side //= 4
        # dp memoize results
        @cache
        def r(used, formed):
            # length of all used matchsticks
            total = 0
            for n in range(len(matchsticks)):
                if not (used & (1 << n)):
                    total += matchsticks[n]
            # check how many sides are formed
            if total and total % side == 0:
                formed += 1
            # if formed three sides success
            if formed == 3:
                return True
            # calculate the remaining space to fill
            remainder = side * (total // side + 1) - total
            # iterate over matchsticks
            for i in range(len(matchsticks)):
                # if matchstick is unused (ie 1) and fits in remaining space
                if used & (1 << i) and matchsticks[i] <= remainder:
                    # mark as used and recurse
                    if r(used ^ (1 << i), formed): return True
            return False
        # create bitmask to represent used matches
        u = 0
        for n in range(len(matchsticks)):
            u |= 1 << n
        return r(u, 0)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,1,2,2,2]
        o = True
        self.assertEqual(s.makesquare(i), o)

    def test_two(self):
        s = Solution()
        i = [3,3,3,3,4]
        o = False
        self.assertEqual(s.makesquare(i), o)

    def test_three(self):
        s = Solution()
        i = [1,1,1]
        o = False
        self.assertEqual(s.makesquare(i), o)

    def test_four(self):
        s = Solution()
        i = [1,1,1,1]
        o = True
        self.assertEqual(s.makesquare(i), o)

    def test_five(self):
        s = Solution()
        i = [10,6,5,5,5,3,3,3,2,2,2,2]
        o = True
        self.assertEqual(s.makesquare(i), o)

    def test_six(self):
        s = Solution()
        i = [2,2,2,2,2,2]
        o = False
        self.assertEqual(s.makesquare(i), o)

    def test_seven(self):
        s = Solution()
        i = [1,2,3,4,5,6,7,8,9,10,5,4,3,2,1]
        o = False
        self.assertEqual(s.makesquare(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)