# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

from sortedcontainers import SortedList

class Solution:
    '''
    Given a binary string s and an integer k.

    In one operation, choose exactly k different indices and flip each '0' to
    '1' and each '1' to '0'.

    Return the minimum number of operations required to make all characters in
    the string equal to '1'. If it is not possible, return -1.
    '''
    # time limit exceeded
    # correct answer however
    def minOperations_tle(self, s: str, k: int) -> int:
        ones = s.count('1')
        zeros = len(s) - ones
        states = set()
        heap = [(0, zeros, ones)]
        while heap:
            steps, zeros, ones = heapq.heappop(heap)
            if zeros == 0 and ones == len(s):
                return steps
            if (zeros, ones) in states:
                continue
            states.add((zeros, ones))
            for i in range(k+1):
                z = i
                o = k - i
                if z <= zeros and o <= ones:
                    heapq.heappush(heap, (steps+1, zeros - z + o, ones - o + z))
                pass
        return -1

    # based on hints
    # moved the nlogn heap insertion behind block
    # still tle
    def minOperations_tle2(self, s: str, k: int) -> int:
        n = len(s)
        zeros = s.count('0')
        visited = set()
        heap = [(0,zeros)]
        while heap:
            steps, zeros = heapq.heappop(heap)
            if zeros == 0:
                return steps
            for i in range(max(0, k - (n - zeros)), min(k, zeros)+1):
                z = zeros + k - 2 * i
                if z not in visited:
                    visited.add(z)
                    heapq.heappush(heap, (steps+1, z))
        return -1

    # based on editorial
    # https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/editorial/?envType=daily-question&envId=2026-02-27
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        zeros = s.count('0')
        steps = [float('inf')] * (n+1)
        steps[zeros] = 0
        evenSet = SortedList(range(0, n+1, 2))
        oddSet = SortedList(range(1, n+1, 2))
        if zeros % 2:
            oddSet.remove(zeros)
        else:
            evenSet.remove(zeros)
        queue = deque([zeros])
        while queue:
            zeros = queue.popleft()
            # minimum number of zeros that can be flipped
            lower = max(k - n + zeros, 0)
            # maximum number of zeros that can be flipped
            upper = min(zeros, k)
            leftBound = zeros + k - 2 * upper
            rightBound = zeros + k - 2 * lower
            s = evenSet if leftBound % 2 == 0 else oddSet
            i = s.bisect_left(leftBound)
            while i < len(s) and s[i] <= rightBound:
                z = s[i]
                steps[z] = steps[zeros] + 1
                queue.append(z)
                s.pop(i)
        return -1 if steps[0] == float('inf') else steps[0]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "110"
        j = 1
        o = 1
        self.assertEqual(s.minOperations(i,j), o)

    def test_two(self):
        s = Solution()
        i = "0101"
        j = 3
        o = 2
        self.assertEqual(s.minOperations(i,j), o)

    def test_three(self):
        s = Solution()
        i = "101"
        j = 2
        o = -1
        self.assertEqual(s.minOperations(i,j), o)

    def test_four(self):
        s = Solution()
        i = "1"
        j = 1
        o = 0
        self.assertEqual(s.minOperations(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)