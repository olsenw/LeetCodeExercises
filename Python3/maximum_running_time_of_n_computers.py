# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There are n computers. Given an integer n and a 0-index integer array
    batteries where the ith battery can run a computer for batteries[i] minutes.
    There is a desire to run all n computers simultaneously using the given
    batteries.

    Initially, it is possible to insert one battery into each computer. After
    and any integer time moment, the battery can be replaced with another
    battery any number of times. The inserted battery can be a totally new
    battery or a battery from another computer. It is assumed that removing and
    inserting a battery takes no time.

    Note that the batteries cannot be recharged.

    Return the maximum number of minutes that all n computers can be
    simultaneously run.
    '''
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        # not needed as constraints prevent
        # # b = len(batteries)
        # # unable to power all n computers
        # if b < n:
        #     return 0
        # # only able to power all computers once
        # if b == n:
        #     return min(batteries)
        
        # way too slow
        def possible_slow(time: int) -> bool:
            b = batteries.copy()
            for _ in range(time):
                b = sorted(b, key=lambda x:-x)
                for i in range(n):
                    if b[i] == 0:
                        return False
                    b[i] -= 1
            return True
        
        # based on leetcode binary search solution
        def possible(time:int)->bool:
            return sum(min(b,time) for b in batteries) // n >= time
            # extra = 0
            # for power in batteries:
            #     extra += min(power, time)
            
            # return extra // n >= time

        # i,j = 1, max(batteries) * len(batteries)
        i,j = 1, sum(batteries) // n
        while i <= j:
            k = (i + j) // 2
            # k = j - (j - i) // 2
            if possible(k):
                answer = k
                i = k + 1
            else:
                j = k - 1
        return answer

    # based on leetcode greedy solution
    def maxRunTime_greedy(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        # largest batteries stuck in computers
        sitting = batteries[-n:]
        # extra power that can be distributed
        floating = sum(batteries[:-n])
        # apply extra power to smallest sitting battery
        for i in range(n-1):
            # not enough extra power to bump up
            if floating // (i+1) < sitting[i+1] - sitting[i]:
                return sitting[i] + floating // (i+1)
            # spend extra power to bump up
            floating -= (i+1) * (sitting[i+1] - sitting[i])
        # see if can bump up above the largest battery
        return sitting[-1] + floating // n

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 2
        j = [3,3,3]
        o = 4
        self.assertEqual(s.maxRunTime(i,j), o)

    def test_two(self):
        s = Solution()
        i = 2
        j = [1,1,1,1]
        o = 2
        self.assertEqual(s.maxRunTime(i,j), o)

    def test_three(self):
        s = Solution()
        i = 1
        j = [2] * (10**5)
        o = 2 * 10**5
        self.assertEqual(s.maxRunTime(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)