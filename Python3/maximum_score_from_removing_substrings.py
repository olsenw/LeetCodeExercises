# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s and two integers x and y. It is possible to perform the
    following two operations any number of times.

    * Remove substring "ab" and gain x points.
    * Remove substring "ba" and gain y points.

    Return the maximum points that can be obtained after applying the above
    operations on s.
    '''
    # right idea but an error with implementation
    def maximumGain_incorrect(self, s: str, x: int, y: int) -> int:
        def cost(s:str, a:str, b:str)->int:
            answer = 0
            stack = ['x']
            for c in s:
                stack.append(c)
                if stack[-2] == a and stack[-1] == b:
                    answer += x
                    stack.pop()
                    stack.pop()
            s = ''.join(stack[1:])
            stack = ['x']
            for c in s:
                stack.append(c)
                if stack[-2] == b and stack[-1] == a:
                    answer += x
                    stack.pop()
                    stack.pop()
            return answer
        if x > y:
            return cost(s, 'a', 'b')
        return cost(s, 'b', 'a')

    def maximumGain_wrong(self, s: str, x: int, y: int) -> int:
        stack = ['x']
        answer = 0
        for c in s:
            stack.append(c)
            while (stack[-2] == 'b' and stack[-1] == 'a') or (stack[-2] == 'a' and stack[-1] == 'b'):
                if x > y:
                    if stack[-2] == 'a' and stack[-1] == 'b':
                        answer += x
                    else:
                        answer += y
                else:
                    if stack[-2] == 'b' and stack[-1] == 'a':
                        answer += y
                    else:
                        answer += x
                stack.pop()
                stack.pop()
        return answer

    def maximumGain(self, s: str, x: int, y: int) -> int:
        answer = 0
        def cost(a,b,v):
            nonlocal answer, s
            stack = ['x','x']
            for c in s:
                stack.append(c)
                while stack[-2] == a and stack[-1] == b:
                    answer += v
                    stack.pop()
                    stack.pop()
            s = ''.join(stack)
        if x < y:
            cost('b', 'a', y)
            cost('a','b', x)
        else:
            cost('a','b', x)
            cost('b', 'a', y)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "cdbcbbaaabab", 4, 5
        o = 19
        self.assertEqual(s.maximumGain(*i), o)

    def test_two(self):
        s = Solution()
        i = "aabbaaxybbaabb", 5, 4
        o = 20
        self.assertEqual(s.maximumGain(*i), o)

    def test_three(self):
        s = Solution()
        i = "ababa", 1, 4
        o = 8
        self.assertEqual(s.maximumGain(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)