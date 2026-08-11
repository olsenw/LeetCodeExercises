# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed array of integers nums.

    A prefix nums[0..i] is sequential if, for all 1 <= j <= i,
    nums[j] = nums[j-1] + 1. In particular, the prefix consisting only of
    nums[0] is sequential.

    Return the smallest integer x missing from nums such that x is greater than
    or equal to the sum of the longest sequential prefix.
    '''
    # stuck... will take longest prefix at any position
    def missingInteger_fails(self, nums: List[int]) -> int:
        n = len(nums)
        answer = 0
        length = 0
        for i in range(n):
            a = nums[i]
            l = 1
            for j in range(i+1, n):
                if nums[j] == nums[j-1] + 1:
                    a += nums[j]
                    l += 1
                else:
                    # if length == l:
                    #     answer = min(answer, a)
                    # elif length < l:
                    if length < l:
                        length = l
                        answer = a
                    break
            # if length == l:
            #     answer = min(answer, a)
            # elif length < l:
            if length < l:
                length = l
                answer = a
        while answer in nums:
            answer += 1
        return answer

    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)
        a = nums[0]
        for i in range(1,n):
            if nums[i] != nums[i-1]+1:
                break
            a += nums[i]
        while a in nums:
            a += 1
        return a

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,2,5]
        o = 6
        self.assertEqual(s.missingInteger(i), o)

    def test_two(self):
        s = Solution()
        i = [3,4,5,1,12,14,13]
        o = 15
        self.assertEqual(s.missingInteger(i), o)

    def test_three(self):
        s = Solution()
        i = [29,30,31,32,33,34,35,36,37]
        o = 297
        self.assertEqual(s.missingInteger(i), o)

    def test_four(self):
        s = Solution()
        i = [4,5,6,7,8,8,9,4,3,2,7]
        o = 30
        self.assertEqual(s.missingInteger(i), o)

    def test_five(self):
        s = Solution()
        i = [46,8,2,4,1,4,10,2,4,10,2,5,7,3,1]
        o = 47
        self.assertEqual(s.missingInteger(i), o)

    def test_six(self):
        s = Solution()
        i = [37,1,2,9,5,8,5,2,9,4]
        o = 38
        self.assertEqual(s.missingInteger(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)