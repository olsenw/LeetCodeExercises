# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums consisting of unique integers.

    Originally, nums contained every integer within a certain range. However, 
    some integers might have gotten removed from the array.

    The smallest and largest integers of the original range are still present in
    nums.

    Return a sorted list of all the missing integers in this range. If no
    integers are missing, return an empty list.
    '''
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        last = nums[0]
        answer = []
        for n in nums:
            for i in range(last+1,n):
                answer.append(i)
            last = n
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,4,2,5]
        o = [3]
        self.assertEqual(s.findMissingElements(i), o)

    def test_two(self):
        s = Solution()
        i = [7,8,6,9]
        o = []
        self.assertEqual(s.findMissingElements(i), o)

    def test_three(self):
        s = Solution()
        i = [5,1]
        o = [2,3,4]
        self.assertEqual(s.findMissingElements(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)