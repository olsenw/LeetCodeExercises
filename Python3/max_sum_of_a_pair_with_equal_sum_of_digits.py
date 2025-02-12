# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed array nums consisting of positive integers. It is possible 
    to choose two indices i and j, such that i != j, and the sum of digits of
    the number nums[i] is equal to that of nums[j].

    Return the maximum value of nums[i] + nums[j] that can be obtained over all
    possible indices i and j that satisfy the conditions.
    '''
    def maximumSum(self, nums: List[int]) -> int:
        def digitSum(num: int) -> int:
            answer = 0
            while num:
                answer += num % 10
                num //= 10
            return answer
        answer = -1
        d = dict()
        for n in nums:
            a = digitSum(n)
            if a in d:
                answer = max(answer, n + d[a])
                if n > d[a]:
                    d[a] = n
            else:
                d[a] = n
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [18,43,36,13,7]
        o = 54
        self.assertEqual(s.maximumSum(i), o)

    def test_two(self):
        s = Solution()
        i = [10,12,19,14]
        o = -1
        self.assertEqual(s.maximumSum(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)