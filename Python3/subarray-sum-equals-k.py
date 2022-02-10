# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an array of integers nums and an integer k, return the total
    number of continuous subarrays whose sum equals k.
    '''
    def subarraySum_brute(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)):
            sum = 0
            for j in nums[i:]:
                sum += j
                if sum == k:
                    ans += 1
        return ans

    def subarraySum_brute_alt(self, nums: List[int], k: int) -> int:
        sums = [0,nums[0]]
        for i in range(1, len(nums)):
            sums.append(nums[i] + sums[i])
        ans = 0
        for i in range(len(sums)):
            for j in range(i):
                if sums[i] - sums[j] == k:
                    ans += 1
        return ans

    # read through the leetcode solution...
    # https://leetcode.com/problems/subarray-sum-equals-k/solution/
    def subarraySum(self, nums: List[int], k: int) -> int:
        from collections import Counter
        c = Counter([0])
        s = 0
        a = 0
        for n in nums:
            s += n
            if s - k in c:
                a += c[s - k]
            c[s] += 1
        return a

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,1,1]
        k = 2
        o = 2
        self.assertEqual(s.subarraySum_brute(i,k), o)
        self.assertEqual(s.subarraySum_brute_alt(i,k), o)
        self.assertEqual(s.subarraySum(i,k), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3]
        k = 3
        o = 2
        self.assertEqual(s.subarraySum_brute(i,k), o)
        self.assertEqual(s.subarraySum_brute_alt(i,k), o)
        self.assertEqual(s.subarraySum(i,k), o)

    def test_three(self):
        s = Solution()
        i = [3,2,1,2,3]
        k = 3
        o = 4
        self.assertEqual(s.subarraySum_brute(i,k), o)
        self.assertEqual(s.subarraySum_brute_alt(i,k), o)
        self.assertEqual(s.subarraySum(i,k), o)

    def test_four(self):
        s = Solution()
        i = [1,-1,0]
        k = 0
        o = 3
        self.assertEqual(s.subarraySum_brute(i,k), o)
        self.assertEqual(s.subarraySum_brute_alt(i,k), o)
        self.assertEqual(s.subarraySum(i,k), o)

    def test_five(self):
        s = Solution()
        i = [3,4,7,2,-3,1,4,2]
        k = 7
        o = 4
        self.assertEqual(s.subarraySum_brute(i,k), o)
        self.assertEqual(s.subarraySum_brute_alt(i,k), o)
        self.assertEqual(s.subarraySum(i,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)