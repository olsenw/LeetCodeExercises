# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    There is a set of integers s, which originally contains all the numbers from
    1 to n. Unfortunately, due to some error, one of the numbers in s got
    duplicated to another number in the the set, which results in repetition of
    one number and loss of another number.

    Given an integer array nums representing the data status of this set after
    the error.

    Find the number that occurs twice and the number that is missing and return
    them in the form of an array.
    '''
    def findErrorNums_sort_wrong(self, nums: List[int]) -> List[int]:
        nums.sort()
        for i in range(len(nums)):
            if i + 1 != nums[i]:
                break
        return [nums[i], i + 1]

    def findErrorNums(self, nums: List[int]) -> List[int]:
        a = None
        s = set()
        for n in nums:
            if n in s:
                a = n
            s.add(n)
        for i in range(1,len(nums)+1):
            if i not in s:
                break
        return [a,i]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,2,4]
        o = [2,3]
        self.assertEqual(s.findErrorNums(i), o)

    def test_two(self):
        s = Solution()
        i = [1,1]
        o = [1,2]
        self.assertEqual(s.findErrorNums(i), o)

    def test_three(self):
        s = Solution()
        i = [1,3,3,4]
        o = [3,2]
        self.assertEqual(s.findErrorNums(i), o)

    def test_four(self):
        s = Solution()
        i = [3,2,3,4,6,5]
        o = [3,1]
        self.assertEqual(s.findErrorNums(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)