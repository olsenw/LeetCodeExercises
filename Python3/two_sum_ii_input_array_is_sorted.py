# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

from bisect import bisect_left

class Solution:
    '''
    Given a 1-indexed array of integers numbers that is already sorted
    in non-decreasing order, find two numbers such that they add up to a
    specific target number. Let these two numbers be numbers[index1] and
    numbers[index2] where 1 <= index1 < index2 <= numbers.length.

    Return the indices of the two numbers, index1 and index2, added by
    one as an integer array [index1, index2] of length 2.

    Note tests are generated such that there is exactly one solution.

    Note use only constant extra space.
    '''
    def twoSum_binary_search(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            t = target - numbers[i]
            # binary search
            j = bisect_left(numbers, t, i + 1)
            if j < len(numbers) and numbers[j] == t:
                return [i + 1, j + 1]

    def twoSum_two_pointer(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            # what the current indices sum up to
            t = numbers[i] + numbers[j]
            # if too large reduce
            if t > target:
                j -= 1
            # if too small increase
            elif t < target:
                i += 1
            # found answer
            else:
                return [i+1,j+1]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,7,11,15]
        j = 9
        o = [1,2]
        self.assertEqual(s.twoSum(i,j), o)

    def test_two(self):
        s = Solution()
        i = [2,3,4]
        j = 6
        o = [1,3]
        self.assertEqual(s.twoSum(i,j), o)

    def test_three(self):
        s = Solution()
        i = [-1,0]
        j = -1
        o = [1,2]
        self.assertEqual(s.twoSum(i,j), o)

    def test_four(self):
        s = Solution()
        i = [3,24,50,79,88,150,345]
        j = 200
        o = [3,6]
        self.assertEqual(s.twoSum(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)