# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed integer array stations of length n, where stations[i]
    represents the number of power stations in the ith city.

    Each power station can provide power to every city in a fixed range. In
    other words, if the range is denoted by r, then a power station at city i
    can provide power to all cites j such that |i - j| <= r and
    0 <= i,j <= n - 1.

    The power of a city is the total number of power stations it is being
    provided power from.

    The government has sanctioned building k more power stations, each of which
    can be built in any city, and have the same range as the pre-existing ones.

    Given the two integers r and k, return the maximum possible minimum power of
    a city, if the additional power stations are built optimally.

    Note that the k power stations can be built in multiple cities.
    '''
    # likely to time out in the line scan
    def maxPower_incomplete(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        power = [0] * n
        queue = deque([])
        for i in range(n):
            while queue and queue[0] + r < i:
                queue.popleft()
            for j in range(stations[i]):
                queue.append(i)
            power[i] = len(queue)
        queue.clear()
        for i in range(n-1, -1, -1):
            while queue and queue[0] - r > i:
                queue.popleft()
            power[i] += len(queue)
            for j in range(stations[i]):
                queue.append(i)
        return

    # unsure how to deal with the binary search to find answer
    def maxPower_incomplete2(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        currentPower = [0] * n
        # store (last index, power)
        heap = []
        # running sum of heap
        power = 0
        for i in range(n):
            while heap and heap[0][0] < i:
                power -= heapq.heappop(heap)[1]
            heapq.heappush(heap, (i + r, stations[i]))
            power += stations[i]
            currentPower[i] = power
        heap = []
        power = 0
        for i in range(n-1,-1,-1):
            while heap and -heap[0][0] > i:
                power -= heapq.heappop(heap)[1]
            currentPower[i] += power
            power += stations[i]
            heapq.heappush(heap, (-(i-r), stations[i]))
        # binary search possible answers
        def test(target:int, k:int) -> bool:
            heap = [(currentPower[i], (1 + min(i + r, n-1) - max(i - r, 0))) for i in range(n)]
            heapq.heapify(heap)
            return False
        i = min(currentPower)
        j = max(currentPower) + k
        while i < j:
            a,b = divmod(j - i, 2)
            m = i + a + b
            if test(m, k):
                i = m
            else:
                j = m - 1
        return i

    # based on Leetcode editorial
    # https://leetcode.com/problems/maximize-the-minimum-powered-city/?envType=daily-question&envId=2025-11-07
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        # the change in power line scan
        baseDiff = [0] * (n+1)
        for i in range(n):
            left = max(0,i-r)
            right = min(n,i+r+1)
            baseDiff[left] += stations[i]
            baseDiff[right] -= stations[i]
        # check if a minimum power is possible
        def test(power:int) -> bool:
            diff = list(baseDiff)
            total = 0
            remaining = k
            for i in range(n):
                total += diff[i]
                if total < power:
                    add = power - total
                    if remaining < add:
                        return False
                    remaining -= add
                    end = min(n, i + 2 * r + 1)
                    diff[end] -= add
                    total += add
            return True
        i = min(stations)
        j = sum(stations) + k
        answer = 0
        while i <= j:
            mid = (i + j) // 2
            if test(mid):
                answer = mid
                i = mid + 1
            else:
                j = mid - 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,4,5,0]
        j = 1
        k = 2
        o = 5
        self.assertEqual(s.maxPower(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = [4,4,4,4]
        j = 0
        k = 3
        o = 4
        self.assertEqual(s.maxPower(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = [0,0,5,0,0]
        j = 2
        k = 5
        o = 10
        self.assertEqual(s.maxPower(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)