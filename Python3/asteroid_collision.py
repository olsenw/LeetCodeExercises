# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array asteroids of integers representing asteroids in a row.

    For each asteroid, the absolute value represents its size, and the sign
    represents its direction (positive meaning right, negative left). Each
    asteroid moves at the same speed.

    Find out the state of the asteroids after all collisions. If two asteroids
    meet, the smaller one will explode. If both are the same size, both will
    explode. Two asteroids moving in the same direction will never meet.
    '''
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        answer = []
        stack = []
        for a in asteroids:
            if a > 0:
                stack.append(a)
            else:
                a = abs(a)
                while stack and stack[-1] < a:
                    stack.pop()
                if stack and stack[-1] == a:
                    stack.pop()
                elif len(stack) == 0:
                    answer.append(-a)
        return answer + stack

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [5,10,-5]
        o = [5,10]
        self.assertEqual(s.asteroidCollision(i), o)

    def test_two(self):
        s = Solution()
        i = [8,-8]
        o = []
        self.assertEqual(s.asteroidCollision(i), o)

    def test_three(self):
        s = Solution()
        i = [10,2,-5]
        o = [10]
        self.assertEqual(s.asteroidCollision(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)