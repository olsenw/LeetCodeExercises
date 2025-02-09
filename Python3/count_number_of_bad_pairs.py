# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed integer array nums. A pair of indices (i,j) is a bad pair
    if i < j and j - i != nums[j] - nums[i].

    Return the total number of bad pairs in nums.
    '''
    def countBadPairs_brute(self, nums: List[int]) -> int:
        n = len(nums)
        answer = 0
        for i in range(n):
            for j in range(i+1, n):
                if j - i != nums[j] - nums[i]:
                    answer += 1
        return answer

    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        d = Counter()
        d[nums[0]] = 1
        answer = 0
        for i in range(1,n):
            x = nums[i] - i
            answer += i - d[x]
            d[x] += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [4,1,3,3]
        o = 5
        self.assertEqual(s.countBadPairs(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,4,5]
        o = 0
        self.assertEqual(s.countBadPairs(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)