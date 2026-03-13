# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer mountainHeight denoting the height of a mountain.

    Also given an integer array workerTimes representing the work time of
    workers in seconds.

    The workers work simultaneously to reduce the height of the mountain. For
    worker i:
    * To decrease the mountain's height by x, it takes workerTimes[i] +
      workerTimes[i] * 2 + ... + workerTimes[i] * x seconds. For example:
      * To reduce the height of the mountain by 1, it takes workerTimes[i]
        seconds.
      * To reduce the height of the mountain by 2, it takes workerTimes[i] +
        workerTimes[i] * 2 seconds and so on.
    
    Return the integer representing the minimum number of seconds required for
    the workers to make the height of the mountain 0.
    '''
    def minNumberOfSeconds_tle(self, mountainHeight: int, workerTimes: List[int]) -> int:
        def check(time:int) -> bool:
            mountain = mountainHeight
            for worker in workerTimes:
                t = time
                x = 1
                while x * worker <= t:
                    mountain -= 1
                    t -= x * worker
                    x += 1
            return mountain <= 0
        i,j = 0, 10**9
        # i,j = 0, 100
        while i < j:
            k = i + (j-i) // 2
            if check(k):
                j = k
            else:
                i = k + 1
        return i

    def minNumberOfSeconds_fails(self, mountainHeight: int, workerTimes: List[int]) -> int:
        workerTimes.sort()
        def check(time:int) -> bool:
            mountain = mountainHeight
            for worker in workerTimes:
                i,j = 0, time
                while i < j:
                    k = i + (j-i+1) // 2
                    if 2 * time >= k * (k+1) * worker:
                        i = k
                    else:
                        j = k - 1
                mountain -= i
                if mountain <= 0:
                    return True
            return False
        # i,j = 1, 5000500000000
        i,j = 1, 10
        while i < j:
            k = i + (j-i) // 2
            if check(k):
                j = k
            else:
                i = k + 1
        return i

    # based on Leetcode editorial
    # https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/editorial/?envType=daily-question&envId=2026-03-13
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        answer = 0
        # minimum bound is one second of work
        i = 1
        # maximum bound is slowest worker and height of mountain (m(m+2)/2)
        j = max(workerTimes) * mountainHeight * (mountainHeight + 1) // 2

        # used to help with rounding issues
        eps = 1e-7

        while i <= j:
            k = i + (j-i) // 2
            
            # figure out how much mountain can be removed in k time
            count = 0
            for t in workerTimes:
                work = k // t
                # largest possible x such that k(k+1)/2 <= work
                # this is done with the quadratic formula
                # editorial explains how this can be derived
                x = int((-1 + (1 + work * 8) ** 0.5) / 2 + eps)
                count += x
            
            # if possible to remove mountain in k time
            if count >= mountainHeight:
                answer = k
                j = k - 1
            else:
                i = k + 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 4
        j = [2,1,1]
        o = 3
        self.assertEqual(s.minNumberOfSeconds(i,j), o)

    def test_two(self):
        s = Solution()
        i = 10
        j = [3,2,2,4]
        o = 12
        self.assertEqual(s.minNumberOfSeconds(i,j), o)

    def test_three(self):
        s = Solution()
        i = 5
        j = [1]
        o = 15
        self.assertEqual(s.minNumberOfSeconds(i,j), o)

    def test_four(self):
        s = Solution()
        i = 1
        j = [10,5,4,10,4,5,3,4,3,1,8,5]
        o = 1
        self.assertEqual(s.minNumberOfSeconds(i,j), o)

    def test_five(self):
        s = Solution()
        i = 10000
        j = [100000]
        o = 5000500000000
        self.assertEqual(s.minNumberOfSeconds(i,j), o)

    def test_six(self):
        s = Solution()
        i = 99
        j = [1,57]
        o = 3916
        self.assertEqual(s.minNumberOfSeconds(i,j), o)

    def test_seven(self):
        s = Solution()
        i = 1
        j = [5]
        o = 5
        self.assertEqual(s.minNumberOfSeconds(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)