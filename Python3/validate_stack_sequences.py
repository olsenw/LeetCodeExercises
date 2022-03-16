# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given two integer arrays pushed and popped each with distinct values
    return true if the could have been the result of a sequence of push
    and pop operations on an intially empty stack, or false otherwise.
    '''
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        for p in pushed:
            stack.append(p)
            while stack and stack[-1] == popped[i]:
                i += 1
                stack.pop()
        return i == len(popped)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,4,5]
        j = [4,5,3,2,1]
        o = True
        self.assertEqual(s.validateStackSequences(i, j), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,4,5]
        j = [4,3,5,1,2]
        o = False
        self.assertEqual(s.validateStackSequences(i, j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)