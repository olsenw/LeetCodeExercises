# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a non-empty array of non-negative integers nums, the degree of this
    array is defined as the maximum frequency of any one of its elements.

    Find the smallest possible length of a contiguous subarray num that has the
    same degree as nums.
    '''
    def findShortestSubArray(self, nums: List[int]) -> int:
        first, last = dict(), dict()
        for i,j in enumerate(nums):
            if j not in first:
                first[j] = i
            last[j] = i
        c = Counter(nums).most_common()
        p = c[0][1]
        answer = len(nums)
        for i,j in c:
            if j < p:
                break
            answer = min(answer, last[i] - first[i] + 1)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,2,3,1]
        o = 2
        self.assertEqual(s.findShortestSubArray(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,2,3,1,4,2]
        o = 6
        self.assertEqual(s.findShortestSubArray(i), o)

    def test_three(self):
        s = Solution()
        i = [1,2,3]
        o = 1
        self.assertEqual(s.findShortestSubArray(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)