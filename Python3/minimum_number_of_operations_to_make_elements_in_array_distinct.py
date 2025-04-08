# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums. Ensure that the elements in the array are
    distinct. To achieve this, perform the following operation any number of
    times:
    * Remove 3 elements from the beginning of the array. If the array has fewer
      than 3 elements, remove all remaining elements.
    
    Note that an empty array is considered to have distinct elements.

    Return the minimum number of operations needed to make the elements in the
    array distinct.
    '''
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        s = set()
        i = n - 1
        # for i in range(n-1,-1,-1):
        while i > -1:
            if nums[i] in s:
                break
            s.add(nums[i])
            i -= 1
        if i == -1:
            return 0
        i += 1
        return (i // 3) + (i % 3 > 0)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,4,2,3,3,5,7]
        o = 2
        self.assertEqual(s.minimumOperations(i), o)

    def test_two(self):
        s = Solution()
        i = [4,5,6,4,4]
        o = 2
        self.assertEqual(s.minimumOperations(i), o)

    def test_three(self):
        s = Solution()
        i = [6,7,8,9]
        o = 0
        self.assertEqual(s.minimumOperations(i), o)

    def test_four(self):
        s = Solution()
        i = [5,5]
        o = 1
        self.assertEqual(s.minimumOperations(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)