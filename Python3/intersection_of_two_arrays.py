# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two integer arrays nums1 and nums2, return an array of their
    intersection. Each element in the result must be unique and may be in any
    order.
    '''
    def intersection_builtin(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))
    
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = set(nums1)
        b = set(nums2)
        if len(b) < len(a):
            a,b = b,a
        answer = []
        for n in a:
            if n in b:
                answer.append(n)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,2,1]
        j = [2,2]
        o = [2]
        self.assertEqual(s.intersection(i,j), o)

    def test_two(self):
        s = Solution()
        i = [4,9,5]
        j = [9,4,9,8,4]
        o = [9,4]
        self.assertEqual(s.intersection(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)