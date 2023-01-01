# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an integer array nums and an integer val, remove all occurrences of
    val in nums in-place. The relative order of the elements may by changed.

    Return k after placing the final result in the first k slots of nums.
    '''
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,2,2,3]
        j = 3
        o = 2
        self.assertEqual(s.removeElement(i,j), o)
        pass

    def test_two(self):
        s = Solution()
        i = [0,1,2,2,3,0,4,2]
        j = 2
        o = 5
        self.assertEqual(s.removeElement(i,j), o)
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)