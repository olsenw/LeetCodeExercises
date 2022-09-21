# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given integer array nums and an array queries where
    queries[i] = [vali, indexi].
    
    For each query i, first apply nums[indexi] = nums[indexi] + vali, then print
    the sum of the even values of nums.

    Return an integer array answer where answer[i] is the answer to the ith
    query.
    '''
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        answer = []
        s = sum(n for n in nums if n % 2 == 0)
        for j,i in queries:
            if nums[i] % 2 == 0:
                s -= nums[i]
            nums[i] += j
            if nums[i] % 2 == 0:
                s += nums[i]
            answer.append(s)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,4]
        j = [[1,0],[-3,1],[-4,0],[2,3]]
        o = [8,6,2,4]
        self.assertEqual(s.sumEvenAfterQueries(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1]
        j = [[4,0]]
        o = [0]
        self.assertEqual(s.sumEvenAfterQueries(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)