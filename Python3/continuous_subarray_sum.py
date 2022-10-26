# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an integer array nums and an integer k, return true if nums has a
    continuous subarray of size at least two whose elements sum up to a multiple
    of k, or false otherwise.

    An integer x is a multiple of k if there exists an integer n such that
    x = n * k. Zero is always a multiple of k.
    '''
    # O(n^2) time
    def checkSubarraySum_brute(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            c = nums[i]
            for j in range(i+1, len(nums)):
                c += nums[j]
                if c % k == 0:
                    return True
        return False

    def checkSubarraySum_wrong(self, nums: List[int], k: int) -> bool:
        c = 0
        h = dict()
        for i in range(len(nums)):
            c = ((nums[i] % k) + (c % k)) % k
            if c in h:
                h[c][1].append(i)
            else:
                h[c] = [0, [i]]
        if 0 in h:
            return True
        c = nums[0] % k
        for i in range(len(nums)):
            t = (k - c) % k
            if t in h:
                while h[t][0] < len(h[t][1]) and h[t][1][h[t][0]] <= i:
                    h[t][0] += 1
                if h[t][0] < len(h[t][1]):
                    return True
            c = ((nums[i] % k) + (c % k)) % k
            pass
        return False

    # Leetcode solution
    # https://leetcode.com/problems/continuous-subarray-sum/solution/
    # O(n) time
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        s = 0
        m = {0:0}
        for i in range(len(nums)):
            s += nums[i]
            if s % k in m:
                if m[s % k] < i:
                    return True
            else:
                m[s % k] = i + 1
        return False

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [23,2,4,6,7]
        j = 6
        o = True
        self.assertEqual(s.checkSubarraySum(i,j), o)

    def test_two(self):
        s = Solution()
        i = [23,2,6,4,7]
        j = 13
        o = False
        self.assertEqual(s.checkSubarraySum(i,j), o)

    def test_three(self):
        s = Solution()
        i = [23,2,6,4,7]
        j = 6
        o = True
        self.assertEqual(s.checkSubarraySum(i,j), o)

    def test_four(self):
        s = Solution()
        i = [24,1]
        j = 6
        o = False
        self.assertEqual(s.checkSubarraySum(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)