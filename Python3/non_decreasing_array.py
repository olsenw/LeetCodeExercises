# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an array nums with n integers check if the array could become
    non-decreasing by modifying at most one element.

    Non-decreasing is defined as nums[i] <= nums[i+1] for every i such
    that 0 <= i <= n-2.
    '''
    def checkPossibility_works(self, nums: List[int]) -> bool:
        def nonDecreasing(start):
            for i in range(start, len(nums) - 1):
                if nums[i] > nums[i+1]:
                    return False
            return True
        for i in range(1, len(nums)-1):
            # good cases
            if nums[i-1] <= nums[i] <= nums[i+1]:
                continue
            # last number less
            elif nums[i+1] < nums[i-1] <= nums[i]:
                nums[i+1] = nums[i]
                return nonDecreasing(i)
            # middle lesser
            elif nums[i] < nums[i-1] <= nums[i+1]:
                nums[i] = nums[i-1]
                return nonDecreasing(i)
            # middle greater
            elif nums[i-1] <= nums[i+1] < nums[i]:
                nums[i] = nums[i-1]
                return nonDecreasing(i)
            # first greater
            elif nums[i-1] > nums[i] and nums[i-1] > nums[i+1] and nums[i] <= nums[i+1]:
                nums[i-1] = nums[i]
                return nonDecreasing(i-1)
            # two decreases 
            elif nums[i-1] > nums[i] > nums[i+1]:
                return False
            else:
                raise Exception("oops")
        return True

    def checkPossibility(self, nums: List[int]) -> bool:
        # determine if non-decreasing
        def nonDecreasing(start):
            for i in range(start, len(nums) - 1):
                if nums[i] > nums[i+1]:
                    return False
            return True
        # special case that first element needs changed
        if len(nums) > 1 and nums[0] > nums[1]:
            return nonDecreasing(1)
        # general case
        for i in range(1, len(nums) - 1):
            # mismatch
            if nums[i] > nums[i+1]:
                # i is out of place
                if nums[i+1] >= nums[i-1]:
                    nums[i] = nums[i-1]
                    return nonDecreasing(i)
                # i+1 is out of place
                elif nums[i-1] <= nums[i]:
                    nums[i+1] = nums[i]
                    return nonDecreasing(i+1)
                # both decrease
                else:
                    return False
        return True

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [4,2,3]
        o = True
        self.assertEqual(s.checkPossibility(i), o)

    def test_two(self):
        s = Solution()
        i = [4,2,1]
        o = False
        self.assertEqual(s.checkPossibility(i), o)

    def test_three(self):
        s = Solution()
        i = [3,4,2,3]
        o = False
        self.assertEqual(s.checkPossibility(i), o)

    def test_four(self):
        s = Solution()
        i = [1]
        o = True
        self.assertEqual(s.checkPossibility(i), o)

    def test_five(self):
        s = Solution()
        i = [5,7,1,8]
        o = True
        self.assertEqual(s.checkPossibility(i), o)

    def test_six(self):
        s = Solution()
        i = [1,2,3]
        o = True
        self.assertEqual(s.checkPossibility(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)