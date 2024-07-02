# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two integer arrays nums1 and nums2, return an array of there
    intersection. Each element in the result must appear as many times as it
    shows in both arrays and the result may be returned in any order.
    '''
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            nums1, nums2 = sorted(nums2), sorted(nums1)
        else:
            nums1, nums2 = sorted(nums1), sorted(nums2)
        answer = []
        i,j = 0,0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                answer.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,2,1]
        j = [2,2]
        o = [2,2]
        self.assertEqual(s.intersect(i,j), o)

    def test_two(self):
        s = Solution()
        i = [4,9,5]
        j = [9,4,9,8,4]
        o = [4,9]
        self.assertEqual(s.intersect(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)