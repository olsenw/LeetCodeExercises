# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two arrays of integers nums and index. Create target array under the
    following rules:
    * Initially target array is empty.
    * From left to right read nums[i] and index[i], insert at index index[i] the
      value nums[i] in target array.
    * Repeat the previous step until there are no elements to read in nums and
      index.
    
    return the target array.

    It is guaranteed that the insertion operations will be valid.
    '''
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        answer = []
        for n,i in zip(nums, index):
            answer.insert(i, n)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [0,1,2,3,4]
        j = [0,1,2,2,1]
        o = [0,4,1,3,2]
        self.assertEqual(s.createTargetArray(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,4,0]
        j = [0,1,2,3,0]
        o = [0,1,2,3,4]
        self.assertEqual(s.createTargetArray(i,j), o)

    def test_three(self):
        s = Solution()
        i = [1]
        j = [0]
        o = [1]
        self.assertEqual(s.createTargetArray(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)