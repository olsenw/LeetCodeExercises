# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed integer array nums and two integers key and k. A k-distant
    index is an index i of nums for which there exists at least one index j such
    that abs(i-j) <= k and nums[j] == key.

    Return a list of all k-distant indices sorted in increasing order.
    '''
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        keys = [i for i in range(len(nums) - 1, -1, -1) if nums[i] == key]
        answer = []
        for i in range(len(nums)):
            pass
            while keys and keys[-1] < i and i - keys[-1] > k:
                keys.pop()
            if keys and abs(i - keys[-1]) <= k:
                answer.append(i)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,4,9,1,3,9,5]
        j = 9
        k = 1
        o = [1,2,3,4,5,6]
        self.assertEqual(s.findKDistantIndices(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = [2,2,2,2,2]
        j = 2
        k = 2
        o = [0,1,2,3,4]
        self.assertEqual(s.findKDistantIndices(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)