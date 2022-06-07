# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given two integer arrays nums1 and nums2, sorted in non-decreasing
    order, and two integers m and n, representing the number of element
    in nums1 and nums2 respectively.

    Merge nums1 and nums2 into a single array sorted in non-decreasing
    order.

    The final sorted array should not be returned by the function, but
    stored inside the array nums1. To accommodate this, nums1 has a
    length of m + n, where the first m elements denote the elements that
    should be merged, and the last n elements are set to 0 and should be
    ignored. nums2 has a length of n.
    '''
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p = m + n - 1
        m -= 1
        n -= 1
        # elements in both lists
        while m >= 0 and n >= 0:
            if nums1[m] >= nums2[n]:
                nums1[p] = nums1[m]
                m -= 1
            else:
                nums1[p] = nums2[n]
                n -= 1
            p -= 1
        # remaining elements in nums1
        pass
        # remaining elements in nums2
        while n >= 0:
            nums1[p] = nums2[n]
            n -= 1
            p -= 1
        return None

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,0,0,0]
        j = 3
        k = [2,5,6]
        l = 3
        o = [1,2,2,3,5,6]
        s.merge(i,j,k,l)
        self.assertEqual(i, o)

    def test_two(self):
        s = Solution()
        i = [1]
        j = 1
        k = []
        l = 0
        o = [1]
        s.merge(i,j,k,l)
        self.assertEqual(i, o)

    def test_three(self):
        s = Solution()
        i = [0]
        j = 0
        k = [1]
        l = 1
        o = [1]
        s.merge(i,j,k,l)
        self.assertEqual(i, o)

if __name__ == '__main__':
    unittest.main(verbosity=2)