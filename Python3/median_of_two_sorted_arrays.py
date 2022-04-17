# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given two sorted arrays nums1 and nums2 of size m and n
    respectively, return the median of the two sorted arrays.

    The overall run time complexity should be O(log(m+n))
    '''

    # O(m + n)
    def findMedianSortedArrays_BRUTE(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
        while i < len(nums1):
            nums.append(nums1[i])
            i += 1
        while j < len(nums2):
            nums.append(nums2[j])
            j += 1
        # now have combined array
        if len(nums) % 2:
            # odd single number is median
            return nums[len(nums) // 2]
        else:
            # even average two numbers is median
            return (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2

    # O((m + n) log (m + n))
    def findMedianSortedArrays_SORT(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        n = len(nums)
        if n % 2:
            return nums[n // 2]
        else:
            return (nums[n // 2] + nums[n // 2 - 1]) / 2

    # O(log(m + n))
    # took reading a bunch of discussion post hints and solutions...
    # derived from clue's answer and stephenweixu's comment
    # https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2511/Intuitive-Python-O(log-(m%2Bn))-solution-by-kth-smallest-in-the-two-sorted-arrays-252ms
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # recursive binary search
        def kth(a, sa, ea, b, sb, eb, k):
            # base cases where an array is empty
            if sa > ea:
                return b[k-sa]
            if sb > eb:
                return a[k-sb]
            # index of pseudo median for arrays
            i, j = (sa + ea) // 2, (sb + eb) // 2
            # values at those indexes
            x, y = a[i], b[j]
            # taken to many (ie k is larger than sum of median indices)
            if i + j < k:
                # if a's median larger than b's median first half does 
                # not include k
                if x > y:
                    return kth(a, sa, ea, b, j + 1, eb, k)
                else:
                    return kth(a, i + 1, ea, b, sb, eb, k)
            # k is smaller than sum of indices
            else:
                # if a's median larger than b's median second half does 
                # not include k
                if x > y:
                    return kth(a, sa, i - 1, b, sb, eb, k)
                else:
                    return kth(a, sa, ea, b, sb, j - 1, k)
        
        m = len(nums1)
        n = len(nums2)
        mn = m + n
        # odd case
        if mn % 2:
            return kth(nums1, 0, m - 1, nums2, 0, n - 1, mn // 2)
        # even case
        else:
            return (kth(nums1, 0, m - 1, nums2, 0, n - 1, mn // 2 - 1)
                     + kth(nums1, 0, m - 1, nums2, 0, n - 1, mn // 2)) / 2

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,3]
        j = [2]
        o = 2.0
        self.assertEqual(s.findMedianSortedArrays_BRUTE(i,j), o)
        self.assertEqual(s.findMedianSortedArrays(i,j), o)
        self.assertEqual(s.findMedianSortedArrays_SORT(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,2]
        j = [3,4]
        o = 2.5
        self.assertEqual(s.findMedianSortedArrays_BRUTE(i,j), o)
        self.assertEqual(s.findMedianSortedArrays(i,j), o)
        self.assertEqual(s.findMedianSortedArrays_SORT(i,j), o)

    def test_three(self):
        s = Solution()
        i = [1,2,3,4,5]
        j = [1,2,3,4,5]
        o = 3.0
        self.assertEqual(s.findMedianSortedArrays_BRUTE(i,j), o)
        self.assertEqual(s.findMedianSortedArrays(i,j), o)
        self.assertEqual(s.findMedianSortedArrays_SORT(i,j), o)

    def test_four(self):
        s = Solution()
        i = [1,2,3,4,5]
        j = [0,6]
        o = 3.0
        self.assertEqual(s.findMedianSortedArrays_BRUTE(i,j), o)
        self.assertEqual(s.findMedianSortedArrays(i,j), o)
        self.assertEqual(s.findMedianSortedArrays_SORT(i,j), o)

    def test_five(self):
        s = Solution()
        i = [1,3,5]
        j = [2,4,6]
        o = 3.5
        self.assertEqual(s.findMedianSortedArrays_BRUTE(i,j), o)
        self.assertEqual(s.findMedianSortedArrays(i,j), o)
        self.assertEqual(s.findMedianSortedArrays_SORT(i,j), o)

    def test_six(self):
        s = Solution()
        i = [1,2,3,4,5]
        j = [6,7]
        o = 4.0
        self.assertEqual(s.findMedianSortedArrays_BRUTE(i,j), o)
        self.assertEqual(s.findMedianSortedArrays(i,j), o)
        self.assertEqual(s.findMedianSortedArrays_SORT(i,j), o)

    def test_seven(self):
        s = Solution()
        i = [1,2,3,4,5]
        j = []
        o = 3.0
        self.assertEqual(s.findMedianSortedArrays_BRUTE(i,j), o)
        self.assertEqual(s.findMedianSortedArrays(i,j), o)
        self.assertEqual(s.findMedianSortedArrays_SORT(i,j), o)

    def test_eight(self):
        s = Solution()
        i = []
        j = [1,2,3,4,5]
        o = 3.0
        self.assertEqual(s.findMedianSortedArrays_BRUTE(i,j), o)
        self.assertEqual(s.findMedianSortedArrays(i,j), o)
        self.assertEqual(s.findMedianSortedArrays_SORT(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)