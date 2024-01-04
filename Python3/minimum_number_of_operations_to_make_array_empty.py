# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed array nums consisting of positive integers.

    There are two types of operations that can be applied any number of times to
    the array:
    * Choose two elements with equal values and delete them from the array.
    * Choose three elements with equal values and delete them from the array.

    Return the minimum number of operations required to make the array empty, or
    -1 if it is not possible.
    '''
    def minOperations_fails(self, nums: List[int]) -> int:
        answer = 0
        c = Counter(nums)
        for i in c:
            if c[i] > 4:
                a,b = divmod(c[i], 3)
                answer += a
                a,b = divmod(c[i], 2)
                answer += a
                if b == 1:
                    return -1
            elif c[i] == 4:
                answer += 2
            elif c[i] == 3:
                answer += 1
            elif c[i] == 2:
                answer += 1
            else:
                return -1
        return answer

    def minOperations(self, nums: List[int]) -> int:
        answer = 0
        c = Counter(nums)
        for i in c:
            a,b = divmod(c[i],3)
            if b == 0:
                answer += a
            elif b == 2 or a > 0:
                answer += a + 1
            else:
                return -1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,3,3,2,2,4,2,3,4]
        o = 4
        self.assertEqual(s.minOperations(i), o)

    def test_two(self):
        s = Solution()
        i = [2,1,2,2,3,3]
        o = -1
        self.assertEqual(s.minOperations(i), o)

    def test_three(self):
        s = Solution()
        i = [14,12,14,14,12,14,14,12,12,12,12,14,14,12,14,14,14,12,12]
        o = 7
        self.assertEqual(s.minOperations(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)