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
    Given a 0-indexed binary string s and two integers minJump and maxJump.
    Starting at index 0, which is equal to '0', it is possible to move from
    index i to index j if the following conditions are fulfilled:
    * i + minJump <= j <= min(i + maxJump, s.length - 1), and
    * s[j] == '0'.

    Return true if it is possible to reach index s.length - 1 in s or false
    otherwise.
    '''
    def canReach_tle(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        @cache
        def dp(index:int) -> bool:
            if index == n - 1:
                return True
            if index >= n:
                return False
            return any(dp(i) for i in range(index + minJump, min(index + maxJump + 1, n)) if s[i] == '0')
        if s[-1] == '1':
            return False
        return dp(0)

    def canReach_tle(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        @cache
        def dp(index:int) -> bool:
            if index == n - 1:
                return True
            if index >= n:
                return False
            return any(dp(i) for i in range(min(index + maxJump, n-1), index + minJump - 1, -1) if s[i] == '0')
        if s[-1] == '1':
            return False
        return dp(0)

    # attempt at sliding window
    def canReach_incorrect(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False
        n = len(s)
        lower = deque([minJump])
        upper = maxJump
        i = 0
        while i < n:
            i = lower.popleft()
            while i < upper and s[i] == '1':
                i += 1
            if s[i] == '1':
                return False
            lower.append(i + minJump)
            upper = min(n-1 , i + maxJump)
        return n-1 <= upper

    def canReach_incorrect(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False
        n = len(s)
        lower = deque([0])
        upper = deque([0])
        i = 0
        while i < n:
            while upper and upper[0] < i:
                upper.popleft()
            while lower and lower[0] < i:
                lower.popleft()
            if not lower:
                return False
            if i < lower[0]:
                i = lower[0]
            if i == n-1:
                return True
            if s[i] == '1':
                i += 1
                continue
            lower.append(min(n-1, i + minJump))
            upper.append(min(n-1, i + maxJump))
            i += 1
        return False

    # Looked at hints to get idea about marking reachable spaces using valid intervals
    # Probably not the best/efficient way however
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False
        n = len(s)
        reachable = [False] * n
        reachable[0] = True
        intervals = deque([(0,0)])
        for i in range(n):
            if intervals[0][1] < i:
                intervals.popleft()
            if not intervals:
                break
            if s[i] == '0' and intervals[0][0] <= i <= intervals[0][1]:
                reachable[i] = True
                intervals.append((i+minJump,i+maxJump))
        return reachable[-1]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "011010"
        j = 2
        k = 3
        o = True
        self.assertEqual(s.canReach(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = "01101110"
        j = 2
        k = 3
        o = False
        self.assertEqual(s.canReach(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = "011111000111000001011111010"
        j = 6
        k = 8
        o = True
        self.assertEqual(s.canReach(i,j,k), o)

    def test_four(self):
        s = Solution()
        i = "00111010"
        j = 3
        k = 5
        o = False
        self.assertEqual(s.canReach(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)