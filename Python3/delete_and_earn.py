# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an integer array nums. Maximize the number of points obtained
    by performing the following operation any number of times:
    
    * Pick any nums[i] and delete it to earn nums[i] points. Afterwards
      delete every element equal to nums[i] - 1 and every element equal
      to nums[i] + 1.

    Return the maximum number of points that can be earned by applying
    the above operation some number of times.
    '''

    # time limit exceeded (14/48 test cases)
    def deleteAndEarn_timeout(self, nums: List[int]) -> int:
        def delete(nums, index):
            return tuple(nums[i] for i in range(len(nums)) if i != index and nums[i] != nums[index] - 1 and nums[i] != nums[index] + 1)
        h = {tuple(nums):0}
        q = [tuple(nums)]
        while q:
            n = []
            for t in q:
                d = {t[i]:i for i in range(len(t))}
                for v in d:
                    x = delete(t, d[v])
                    if x in h:
                        h[x] = max(h[x], h[t] + v)
                    else:
                        h[x] = h[t] + v
                    n.append(x)
            q = n
        return h[()]

    # time limit exceeded (23/48 test cases)
    def deleteAndEarn_timeout2(self, nums: List[int]) -> int:
        from collections import Counter
        h = {tuple(nums):0}
        q = [tuple(nums)]
        while q:
            n = []
            for t in q:
                c = Counter(t)
                for v in list(c.keys()):
                    x, y, z = c[v-1], c[v+1], c[v]
                    c[v-1], c[v+1], c[v] = 0, 0, 0
                    a = tuple(c.elements())
                    if a in h:
                        h[a] = max(h[a], h[t] + v * z)
                    else:
                        h[a] = h[t] + v * z
                    n.append(a)
                    c[v-1], c[v+1], c[v] = x, y, z
            q = n
        return h[()]

    # time limit exceeded (23/48 test cases)
    def deleteAndEarn_timeout3(self, nums: List[int]) -> int:
        from collections import Counter
        def delete(c, v):
            return tuple(i for i in c if i != v and i != v-1 and i != v+1)
        c = Counter(nums)
        d = {delete(c, i): i * c[i] for i in c}
        q = list(d.keys())
        while q:
            n = []
            for t in q:
                for v in t:
                    a = delete(t,v)
                    if a in d:
                        d[a] = max(d[a], d[t] + v * c[v])
                    else:
                        d[a] = d[t] + v * c[v]
                    n.append(a)
            q = n
        return d[()]

    # took awhile for the hint to make sense...
    # bottom up dynamic programming approach
    # from smallest to largest num in nums decide whether to take num
    # based on previous answers of [0:num-1] and [0:num-2] subsets
    def deleteAndEarn(self, nums: List[int]) -> int:
        from collections import Counter
        # how many points a given number is worth (takes all of number)
        c = Counter(nums)
        for i in c:
            c[i] *= i
        values = sorted(c.keys())
        # tracks max value of taking/not taking a number
        dp = Counter({values[0]:c[values[0]]})
        # manually find max for every value (smallest -> largest)
        for i in range(1,len(values)):
            v = values[i]
            # make choice if take or not (ie have v and v-1)
            if v == values[i-1] + 1:
                # always on the right most side so don't worry about v+1
                # if take v can also take v-2 (one less than deleted value)
                # if don't take v can take previous v-1
                dp[v] = max(c[v] + dp[values[i-2]], dp[v-1])
            # no conflict so just take (no conflict between v and last value)
            else:
                dp[v] = c[v] + dp[values[i-1]]
        # maximum value
        return dp[values[-1]]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,4,2]
        o = 6
        self.assertEqual(s.deleteAndEarn(i), o)

    def test_two(self):
        s = Solution()
        i = [2,2,3,3,3,4]
        o = 9
        self.assertEqual(s.deleteAndEarn(i), o)

    def test_three(self):
        s = Solution()
        i = [1,1,1,2,4,5,5,5,6]
        o = 18
        self.assertEqual(s.deleteAndEarn(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)