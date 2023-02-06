# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given the array nums consisting of 2n elements in the form
    [x1,x2,...,xn,y1,y2,...,yn].

    Return the array in the form [x1,y1,x2,y2,...,xn,yn]
    '''
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        a = []
        for i,j in zip(nums[:n],nums[n:]):
            a.append(i)
            a.append(j)
        return a

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,5,1,3,4,7]
        j = 3
        o = [2,3,5,4,1,7] 
        self.assertEqual(s.shuffle(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,4,4,3,2,1]
        j = 4
        o = [1,4,2,3,3,2,4,1]
        self.assertEqual(s.shuffle(i,j), o)

    def test_three(self):
        s = Solution()
        i = [1,1,2,2]
        j = 2
        o = [1,2,1,2]
        self.assertEqual(s.shuffle(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)