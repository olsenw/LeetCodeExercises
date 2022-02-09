# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an array of integers nums and an integer k, return the number
    of unique k-diff pairs in the array.

    A k-diff pair is an integer pair (nums[i], nums[j]), where the 
    following are true:
    * 0 <= i < j < nums.length
    * abs(nums[i] - nums[j]) == k
    '''
    def findPairs_brute(self, nums: List[int], k: int) -> int:
        ans = 0
        unique = set()
        # print()
        for i, ni in enumerate(nums):
            for j, nj in enumerate(nums[i+1:], i+1):
                t = tuple(sorted([ni,nj]))
                if abs(ni-nj) == k and t not in unique:
                    # print(t)
                    unique.add(t)
                    ans += 1
        return ans

    def findPairs_count(self, nums: List[int], k: int) -> int:
        # vvvvvvv - works (fastest) - vvvvvvv
        from collections import Counter
        c = Counter(nums)
        ans = 0
        for i in sorted(c.keys()):
            if k:
                if i+k in c:
                    ans += 1
            else:
                if c[i] > 1:
                    ans += 1
        return ans
        # vvvvvvv - works - vvvvvvv
        # from collections import Counter
        # c = Counter(nums)
        # ans = 0
        # alt = 0
        # for i in c:
        #     ans += min(c[i-k], 1) + min(c[i+k], 1)
        #     alt += 1 if c[i] > 1 else 0
        # return ans // 2 if k else alt
        # vvvvvvv - too slow - vvvvvvv
        # from collections import Counter
        # ans = 0
        # cnt = Counter(nums)
        # key = list(cnt)
        # for i, n in enumerate(key):
        #     for j in key[i:]:
        #         if (n != j and abs(n-j) == k) or (n == j and cnt[n] > 1 and k == 0):
        #             ans += 1
        # return ans

    def findPairs_sort(self, nums: List[int], k: int) -> int:
        nums.sort()
        seen = dict()
        for i, n in enumerate(nums):
            if n not in seen:
                seen[n] = i
        ans = 0
        for i in seen:
            if i + k in seen:
                ans += 1 if k else 1 if seen[i]+1 < len(nums) and i == nums[seen[i]+1] else 0
        return ans

    # this is 85% on leetcode
    def findPairs_playing(self, nums: List[int], k: int) -> int:
        seen = set()
        valid = set()
        nums.sort()
        for i in nums:
            if i-k in seen:
                valid.add(i)
            seen.add(i)
        return len(valid)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,1,4,1,5]
        k = 2
        o = 2
        self.assertEqual(s.findPairs_playing(i, k), o)
        self.assertEqual(s.findPairs_brute(i, k), o)
        self.assertEqual(s.findPairs_count(i, k), o)
        self.assertEqual(s.findPairs_sort(i, k), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,4,5]
        k = 1
        o = 4
        self.assertEqual(s.findPairs_playing(i, k), o)
        self.assertEqual(s.findPairs_brute(i, k), o)
        self.assertEqual(s.findPairs_count(i, k), o)
        self.assertEqual(s.findPairs_sort(i, k), o)

    def test_three(self):
        s = Solution()
        i = [1,3,1,5,4]
        k = 0
        o = 1
        self.assertEqual(s.findPairs_playing(i, k), o)
        self.assertEqual(s.findPairs_brute(i, k), o)
        self.assertEqual(s.findPairs_count(i, k), o)
        self.assertEqual(s.findPairs_sort(i, k), o)

    def test_four(self):
        s = Solution()
        i = [1,2,4,4,3,3,0,9,2,3]
        k = 3
        o = 2
        self.assertEqual(s.findPairs_playing(i, k), o)
        self.assertEqual(s.findPairs_brute(i, k), o)
        self.assertEqual(s.findPairs_count(i, k), o)
        self.assertEqual(s.findPairs_sort(i, k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)