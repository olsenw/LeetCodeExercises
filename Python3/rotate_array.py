# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an array, rotate the array to the right by k steps, where k is
    non-negative.
    '''
    # O(n) time
    # O(n) space
    # create a duplicate array to index out of
    def rotate_duplicate(self, nums: List[int], k: int) -> None:
        swap = list(nums)
        i = 0
        k = k % len(nums)
        while i < len(nums):
            nums[k] = swap[i]
            i += 1
            k = k + 1 if k+1 < len(nums) else 0

    # O(n^2) time (fails leetcode - time exceeded)
    # O(1) space
    # make use of a single temp variable to rotate in place
    def rotate_temp(self, nums: List[int], k: int) -> None:
        temp = 0
        for i in range(k % len(nums)):
            temp = nums[-1]
            for j in range(len(nums) - 1, 0, -1):
                nums[j] = nums[j-1]
            nums[0] = temp

    # O(n) time
    # O(k%len(n)) space
    # make use of a k temp variables to rotate in place
    # if k is large enough basically rotate_duplicate
    def rotate_k_temp(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        temp = [nums[i] for i in range(len(nums)-k, len(nums))]
        for i in range(len(nums) - 1, k - 1, -1):
            nums[i] = nums[i-k]
        for i in range(k):
            nums[i] = temp[i]

    # this makes use of python's list index features to create a list
    # from two views of nums
    # idea from a sample leetcode solution, similar idea to above
    def rotate_slick(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]

class UnitTesting(unittest.TestCase):
    def __tester(self, l, k, c, r):
        s = Solution()
        r(s,l,k)
        self.assertEqual(l, c)

    def test_one(self):
        i = [1,2,3,4,5,6,7]
        k = 3
        o = [5,6,7,1,2,3,4]
        self.__tester(list(i), k, o, Solution.rotate_duplicate)
        self.__tester(list(i), k, o, Solution.rotate_temp)
        self.__tester(list(i), k, o, Solution.rotate_k_temp)
        self.__tester(list(i), k, o, Solution.rotate_slick)

    def test_two(self):
        i = [-1,-100,3,99]
        k = 2
        o = [3,99,-1,-100]
        self.__tester(list(i), k, o, Solution.rotate_duplicate)
        self.__tester(list(i), k, o, Solution.rotate_temp)
        self.__tester(list(i), k, o, Solution.rotate_k_temp)
        self.__tester(list(i), k, o, Solution.rotate_slick)

    def test_three(self):
        i = [-1,-100,3,99,1]
        k = 2
        o = [99,1,-1,-100,3]
        self.__tester(list(i), k, o, Solution.rotate_duplicate)
        self.__tester(list(i), k, o, Solution.rotate_temp)
        self.__tester(list(i), k, o, Solution.rotate_k_temp)
        self.__tester(list(i), k, o, Solution.rotate_slick)

    def test_four(self):
        i = [1,2,3,4,5,6]
        k = 3
        o = [4,5,6,1,2,3]
        self.__tester(list(i), k, o, Solution.rotate_duplicate)
        self.__tester(list(i), k, o, Solution.rotate_temp)
        self.__tester(list(i), k, o, Solution.rotate_k_temp)
        self.__tester(list(i), k, o, Solution.rotate_slick)

    def test_five(self):
        i = [1,2,3]
        k = 2
        o = [2,3,1]
        self.__tester(list(i), k, o, Solution.rotate_duplicate)
        self.__tester(list(i), k, o, Solution.rotate_temp)
        self.__tester(list(i), k, o, Solution.rotate_k_temp)
        self.__tester(list(i), k, o, Solution.rotate_slick)

if __name__ == '__main__':
    unittest.main(verbosity=2)