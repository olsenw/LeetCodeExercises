# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an array nums of n positive integers.

    It is possible to preform two types of operations on any element of 
    nums array any number of times:
    * if the element is even, may divide it by 2 (ie 12 -> 6 -> 3)
    * if the element is odd, multiply it by 2 (ie 1 -> 2, 5 -> 10)

    The deviation of the array is the maximum difference between any two
    elements in the array.

    Return the minimum deviation the array can have after perfroming 
    some number of operations.
    '''
    # based on solution by DBabichev
    # https://leetcode.com/problems/minimize-deviation-in-array/discuss/1041766/Python-Heap-solution-explained
    def minimumDeviation_discussions(self, nums: List[int]) -> int:
        import heapq
        numMinMax = []
        for n in nums:
            m = n
            while not m % 2:
                m //= 2
            numMinMax.append((m, max(n, m*2)))
        m = max(i for i,_ in numMinMax)
        heapq.heapify(numMinMax)
        deviation = 2**31
        while True:
            n, l = numMinMax[0]
            deviation = min(deviation, m-n)
            if n < l:
                heapq.heapreplace(numMinMax, (n*2, l))
                m = max(m, n*2)
            else:
                break
        return deviation

    # first attempt
    # somewhere there is a disconnect that occurs...
    # not working with enough information maybe...
    # passes 73/76 test cases on leetcode...
    def minimumDeviation_fails(self, nums: List[int]) -> int:
        import heapq
        #
        # here to next block is issue
        # do not keep track of lowest possible
        # also needs to be done after maximum
        #
        nums = [n * -1 for n in nums]
        heapq.heapify(nums)
        while not nums[0] % 2:
            heapq.heapreplace(nums, nums[0] // 2)
        nums = [n * -1 for n in nums]
        #
        # here on is correct for finding max
        # but starting deviation here misses early on possibles
        #
        m = nums[0]
        heapq.heapify(nums)
        deviation = m - nums[0]
        while nums[0] % 2 and abs(nums[0] * 2 - m) <= m - nums[0]:
            m = max(m, nums[0] * 2)
            heapq.heapreplace(nums, nums[0] * 2)
            deviation = min(deviation, m - nums[0])
        return deviation

    # corrected version after gaining further understanding
    def minimumDeviation_corrected(self, nums: List[int]) -> int:
        import heapq
        # maximum (biggest possible ever can be)
        m = max(nums)
        heapq.heapify(nums)
        deviation = m - nums[0]
        while nums[0] % 2: # while odd
            m = max(m, nums[0] * 2)
            heapq.heapreplace(nums, nums[0] * 2)
            deviation = min(deviation, m - nums[0])
        # minimum (smallest possible ever can be)
        # has to occur after finding maximum because can divide the 
        # multiply by 2, but can't necessarily multiply the division
        l = nums[0]
        nums = [-n for n in nums]
        heapq.heapify(nums)
        while not nums[0] % 2: # while even
            l = min(l, -nums[0] // 2)
            heapq.heapreplace(nums, nums[0] // 2)
            deviation = min(deviation, -nums[0] - l)
        return deviation

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,4]
        o = 1
        self.assertEqual(s.minimumDeviation_discussions(i), o)
        i = [1,2,3,4]
        self.assertEqual(s.minimumDeviation_corrected(i), o)

    def test_two(self):
        s = Solution()
        i = [4,1,5,20,3]
        o = 3
        self.assertEqual(s.minimumDeviation_discussions(i), o)
        i = [4,1,5,20,3]
        self.assertEqual(s.minimumDeviation_corrected(i), o)

    def test_three(self):
        s = Solution()
        i = [2,10,8]
        o = 3
        self.assertEqual(s.minimumDeviation_discussions(i), o)
        i = [2,10,8]
        self.assertEqual(s.minimumDeviation_corrected(i), o)

    def test_four(self):
        s = Solution()
        i = [15,5,3,10]
        o = 9
        self.assertEqual(s.minimumDeviation_discussions(i), o)
        i = [15,5,3,10]
        self.assertEqual(s.minimumDeviation_corrected(i), o)

    def test_five(self):
        s = Solution()
        i = [1,1,1,1]
        o = 0
        self.assertEqual(s.minimumDeviation_discussions(i), o)
        i = [1,1,1,1]
        self.assertEqual(s.minimumDeviation_corrected(i), o)

    def test_six(self):
        s = Solution()
        i = [3,5]
        o = 1
        self.assertEqual(s.minimumDeviation_discussions(i), o)
        i = [3,5]
        self.assertEqual(s.minimumDeviation_corrected(i), o)

    def test_seven(self):
        s = Solution()
        i = [399,908,648,357,693,502,331,649,596,698]
        o = 315
        self.assertEqual(s.minimumDeviation_discussions(i), o)
        i = [399,908,648,357,693,502,331,649,596,698]
        self.assertEqual(s.minimumDeviation_corrected(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)