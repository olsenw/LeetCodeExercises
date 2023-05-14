# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
from math import gcd
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given nums, an array of positive integers of size 2 * n. Perform n
    operations on this array.

    In the ith operation (1-indexed):
    * Choose two elements x and y.
    * Receive a score of i * gcd(x,y).
    * Remove x and y from nums.

    Return the maximum score that can be obtained after preforming n operations.

    The function gcd(x,y) is the greatest common divisor of x and y.
    '''
    # correct... but way to slow
    def maxScore_tle(self, nums: List[int]) -> int:
        n = len(nums) // 2
        g = [(i,j,gcd(nums[i],nums[j])) for i in range(len(nums)) for j in range(i+1,len(nums))]
        taken = set()
        def r(i,j):
            if i == len(g) or j > n:
                return 0
            a,b,c = g[i]
            x = r(i + 1, j)
            if a in taken or b in taken:
                return x
            taken.add(a)
            taken.add(b)
            y = j * c + r(i + 1, j + 1)
            taken.remove(a)
            taken.remove(b)
            return max(x,y)
        return r(0,1)

    # based on leetcode hint of greedily take largest gcd
    # not quite right but very close
    def maxScore_incorrect(self, nums: List[int]) -> int:
        n = len(nums) // 2
        g = [(i,j,gcd(nums[i],nums[j])) for i in range(len(nums)) for j in range(i+1,len(nums))]
        answer = 0
        while n > 0:
            # issue is here
            # what happens if there is a tie for gcd
            # need to take the one that has worst follow up
            # ie one that does note reduce the following step
            a,b,c = max(g, key=lambda x: (x[2],-x[0],-x[1]))
            answer += n * c
            pass
            g = [i for i in g if i[0] != a and i[0] != b and i[1] != a and i[1] != b]
            n -= 1
        return answer

    # still off
    def maxScore_still_incorrect(self, nums: List[int]) -> int:
        def r(g: List,t):
            if t == 0:
                return 0
            answer = 0
            g.sort(key=lambda x: (-x[2],x[0],x[1]))
            best = g[0][2]
            for a,b,c in g:
                if c < best:
                    break
                answer = max(answer, t * c + r([i for i in g if i[0] != a and i[0] != b and i[1] != a and i[1] != b],t-1))
            return answer
        return r([(i,j,gcd(nums[i],nums[j])) for i in range(len(nums)) for j in range(i+1,len(nums))], len(nums) // 2)

    # very slow (barely passes the test)
    # a bit mask for the various combinations may be better than the tuple...
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums) // 2
        @cache
        def r(g, t):
            if t == 0:
                return 0
            answer = 0
            for a,b,c in g:
                answer = max(
                    answer,
                    t * c + r(tuple(i for i in g if i[0] != a and i[0] != b and i[1] != a and i[1] != b), t-1)
                )
            return answer
        return r(tuple((i,j,gcd(nums[i],nums[j])) for i in range(len(nums)) for j in range(i+1,len(nums))), n)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2]
        o = 1
        self.assertEqual(s.maxScore(i), o)

    def test_two(self):
        s = Solution()
        i = [3,4,6,8]
        o = 11
        self.assertEqual(s.maxScore(i), o)

    def test_three(self):
        s = Solution()
        i = [1,2,3,4,5,6]
        o = 14
        self.assertEqual(s.maxScore(i), o)

    def test_four(self):
        s = Solution()
        i = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
        o = 138
        self.assertEqual(s.maxScore(i), o)

    def test_five(self):
        s = Solution()
        i = [655942, 98097, 786127, 991508, 257619, 289959, 388650, 163009, 569883, 343426, 358744, 143087, 120347, 349645]
        o = 552
        self.assertEqual(s.maxScore(i), o)

    def test_six(self):
        s = Solution()
        i = [109497,983516,698308,409009,310455,528595,524079,18036,341150,641864,913962,421869,943382,295019]
        o = 527
        self.assertEqual(s.maxScore(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)