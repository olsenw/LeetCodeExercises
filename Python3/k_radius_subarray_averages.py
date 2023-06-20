# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed array nums of n integers, and an integer k.

    The k-radius average for a subarray of nums centered at some index i with
    the radius k is the average of all elements in nums between the indices
    i - k and i + k (inclusive). If there are less than k elements before or
    after the index i, the the k-radius average is -1.

    Build and return an array avgs of length n where avgs[i] is the k-radius
    average for the subarray centered at index i.

    The average of x elements is the sum of the x elements divided by x, using
    integer division. The integer division truncates toward zero, which means
    losing its fractional part.
    '''
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        nums.append(0)
        answer = [-1] * n
        s = sum(nums[:2*k+1])
        for i in range(k, n - k):
            answer[i] = s // (2 * k + 1)
            s -= nums[i - k]
            s += nums[i + k + 1]
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [7,4,3,9,1,8,5,2,6]
        j = 3
        o = [-1,-1,-1,5,4,4,-1,-1,-1]
        self.assertEqual(s.getAverages(i,j), o)

    def test_two(self):
        s = Solution()
        i = [100000]
        j = 0
        o = [100000]
        self.assertEqual(s.getAverages(i,j), o)

    def test_three(self):
        s = Solution()
        i = [8]
        j = 100000
        o = [-1]
        self.assertEqual(s.getAverages(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)