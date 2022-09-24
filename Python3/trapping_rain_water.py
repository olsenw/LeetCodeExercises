# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given n non-negative integers representing an elevation map where the width
    of each bar is 1, compute how much water it can trap after raining.
    '''
    def trap_monotonic(self, height: List[int]) -> int:
        a = 0
        mono = []
        for i, h in enumerate(height):
            n = 0
            for j in range(len(mono) - 1, -1, -1):
                if mono[j][0] <= h:
                    a += (mono[j][0] - n) * (i - mono[j][1] - 1)
                    n = mono.pop()[0]
                elif n < h and mono[j][0] > h:
                    a += (h - n) * (i - mono[j][1] - 1)
                    break
                else:
                    break
            if h:
                mono.append((h,i))
        return a

    # based on leetcode solution
    def trap_dp(self, height: List[int]) -> int:
        # length of height array
        n = len(height)
        # dp for max height going left from position i
        left = [0] * n
        left[0] = height[0]
        for i in range(1, n):
            left[i] = max(left[i-1], height[i])
        # dp for max height going right from position i
        right = [0] * n
        right[-1] = height[-1]
        for i in range(n-2,-1,-1):
            right[i] = max(right[i+1], height[i])
        # for each index i calculate how much water could be stored at i
        answer = 0
        for i in range(1, n-1):
            answer += min(left[i], right[i]) - height[i]
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [0,1,0,2,1,0,1,3,2,1,2,1]
        o = 6
        self.assertEqual(s.trap(i), o)

    def test_two(self):
        s = Solution()
        i = [4,2,0,3,2,5]
        o = 9
        self.assertEqual(s.trap(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)