# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of integers nums of length n and a positive integer k.

    The power of an array is defined as:
    * Its maximum element if all of its elements are consecutive and sorted in
      ascending order.
    * -1 otherwise.

    Find the power of all subarrays of nums of size k.

    Return an integer array results of size n - k + 1, where results[i] is the
    power of nums[1..(i + k - 1)].
    '''
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        answer = []
        n = 1
        i = 0
        for i in range(1,k-1):
            if nums[i] == nums[i-1] + 1:
                n += 1
            else:
                n = 1
        # if k == 1:
        #     answer.append(nums[0])
        pass
        for i in range(max(1, k-1), len(nums)):
            if nums[i] == nums[i-1] + 1:
                if n < k:
                    n += 1
                if n == k:
                    answer.append(nums[i])
                else:
                    answer.append(-1)
            else:
                answer.append(-1)
                n = 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,4,3,2,5]
        j = 3
        o = [3,4,-1,-1,-1]
        self.assertEqual(s.resultsArray(i,j), o)

    def test_two(self):
        s = Solution()
        i = [2,2,2,2,2]
        j = 4
        o = [-1,-1]
        self.assertEqual(s.resultsArray(i,j), o)

    def test_three(self):
        s = Solution()
        i = [3,2,3,2,3,2]
        j = 2
        o = [-1,3,-1,3,-1]
        self.assertEqual(s.resultsArray(i,j), o)

    def test_four(self):
        s = Solution()
        i = [1]
        j = 1
        o = [1]
        self.assertEqual(s.resultsArray(i,j), o)

    def test_five(self):
        s = Solution()
        i = [1,2]
        j = 1
        o = [1,2]
        self.assertEqual(s.resultsArray(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)