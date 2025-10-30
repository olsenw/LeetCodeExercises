# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array target. Also given is an integer array initial of the
    same length as target with all element initially zeros.

    In one operation choose any subarray from initial and increment each value
    by one.

    Return the minimum number of operations to form a target array from initial.

    The test cases are generated so that the answer fits in a 32-bit integer.
    '''
    def minNumberOperations(self, target: List[int]) -> int:
        answer = 0
        target.append(0)
        stack = [0]
        for t in target:
            while t < stack[-1]:
                answer += stack[-1] - max(t,stack[-2])
                stack.pop()
            if t > stack[-1]:
                stack.append(t)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,2,1]
        o = 3
        self.assertEqual(s.minNumberOperations(i), o)

    def test_two(self):
        s = Solution()
        i = [3,1,1,2]
        o = 4
        self.assertEqual(s.minNumberOperations(i), o)

    def test_three(self):
        s = Solution()
        i = [3,1,5,4,2]
        o = 7
        self.assertEqual(s.minNumberOperations(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)