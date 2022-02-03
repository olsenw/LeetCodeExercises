# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given four integer arrays nums1, nums2, nums3, and nums4 all of 
    length n, return the number of tuples (i, j, k, l) such that:
    * 0 <= i, j, k, l < n
    * nums1[i] + nums2[j] + nums3[k] + nums4[k] == 0
    '''
    # O(n^4) time
    def fourSumCount_brute(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        ans = 0
        n = len(nums1)
        c = 0
        for i1 in nums1:
            for i2 in nums2:
                for i3 in nums3:
                    for i4 in nums4:
                        c += 1
                        if i1 + i2 + i3 + i4 == 0:
                            ans += 1
        print(f"\nbrute {c}")
        return ans

    # the sets undercount... need to know all possible
    # idea bears merit which is why it is left here
    def fourSumCount_broken(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        possible = lambda s1, s2: {i + j for i in s1 for j in s2}
        ans = 0
        # c = 0
        for p in possible(possible(set(nums1), set(nums2)), set(nums3)):
            for k in set(nums4):
                # c += 1
                if p + k == 0:
                    ans += 1
        # print(f"\nsets {c}")
        return ans

    # barley passes
    # whole bunch of extra calculation...
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        from collections import Counter
        def possible(cnt, lst):
            n = Counter()
            for c in cnt:
                for l in lst:
                    n[c + l] += cnt[c]
            return n
        return possible(possible(possible(Counter(nums1), nums2),nums3),nums4)[0]

    # zhuow solution really fast
    # https://leetcode.com/problems/4sum-ii/discuss/1740492/Python-in-2-lines
    # similar base idea, much smarter execution of problem space
    def fourSumCount_leetcode(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        from collections import Counter
        # all the possible options for nums1 + nums2 
        c = Counter(a+b for a in nums1 for b in nums2)
        # then again for nums3 + nums4
        # where we sum up the counter that matches (counter defaults 0)
        return sum(c[-c-d] for c in nums3 for d in nums4)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i1 = [1,2]
        i2 = [-2,-1]
        i3 = [-1,2]
        i4 = [0,2]
        o = 2
        self.assertEqual(s.fourSumCount_brute(i1, i2, i3, i4), o)
        self.assertEqual(s.fourSumCount(i1, i2, i3, i4), o)
        self.assertEqual(s.fourSumCount_revised(i1, i2, i3, i4), o)

    def test_two(self):
        s = Solution()
        i1 = [0]
        i2 = [0]
        i3 = [0]
        i4 = [0]
        o = 1
        self.assertEqual(s.fourSumCount_brute(i1, i2, i3, i4), o)
        self.assertEqual(s.fourSumCount(i1, i2, i3, i4), o)
        self.assertEqual(s.fourSumCount_revised(i1, i2, i3, i4), o)

    def test_three(self):
        s = Solution()
        i1 = [i+1000 for i in range(100)]
        i2 = [i for i in range(100)]
        i3 = [i for i in range(100)]
        i4 = [i for i in range(100)]
        o = 0
        # self.assertEqual(s.fourSumCount_brute(i1, i2, i3, i4), o)
        self.assertEqual(s.fourSumCount(i1, i2, i3, i4), o)
        self.assertEqual(s.fourSumCount_revised(i1, i2, i3, i4), o)

    def test_four(self):
        s = Solution()
        i1 = [-1,-1]
        i2 = [-1,1]
        i3 = [-1,1]
        i4 = [1,-1]
        o = 6
        self.assertEqual(s.fourSumCount_brute(i1, i2, i3, i4), o)
        self.assertEqual(s.fourSumCount(i1, i2, i3, i4), o)
        self.assertEqual(s.fourSumCount_revised(i1, i2, i3, i4), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)