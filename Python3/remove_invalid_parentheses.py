# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s that contains parentheses and letters, remove the minimum
    number of invalid parentheses to make the input string valid.

    Return a list of unique strings that are valid with the minimum number of
    removals. The answer may be returned in any order.
    '''
    def removeInvalidParentheses_fails(self, s: str) -> list[str]:
        answer = []
        def valid(s: str) -> bool:
            left = 0
            for c in s:
                if c == '(':
                    left += 1
                elif c == ')':
                    left -= 1
                    if left < 0:
                        return False
            if left == 0:
                answer.append(s)
                return True
            return False
        @cache
        def dfs(s: str) -> None:
            if valid(s):
                return
            for i in range(len(s)):
                dfs(s[:i] + s[i+1:])
            return
        dfs(s)
        return answer

    def removeInvalidParentheses_fails(self, s: str) -> list[str]:
        def valid(s: str) -> bool:
            left = 0
            for c in s:
                if c == '(':
                    left += 1
                elif c == ')':
                    left -= 1
                    if left < 0:
                        return False
            return left == 0
        answer = []
        queue = [(-len(s), s)]
        seen = set()
        while queue:
            length, word = heapq.heappop(queue)
            if word in seen:
                continue
            seen.add(word)
            if valid(word):
                answer.append(word)
                continue
            for i in range(-length):
                w = word[:i] + word[i+1:]
                if w not in seen:
                    heapq.heappush(queue, (-len(w), w))
        return answer

    @cache
    def removeInvalidParentheses(self, s: str) -> list[str]:
        # check if input is a valid string
        def valid(s:str) -> bool:
            left = 0
            for c in s:
                if c == '(':
                    left += 1
                elif c == ')':
                    left -= 1
                    if left < 0:
                        return False
            return left == 0
        if valid(s):
            return [s]
        # there must be an invalid parentheses
        seen = set()
        answer = []
        n = 0
        for i in range(len(s)):
            a = self.removeInvalidParentheses(s[:i] + s[i+1:])
            m = 0
            for w in a:
                m = max(m, len(w))
                if w in seen:
                    continue
                seen.add(w)
                if answer and n < m:
                    answer = []
                if len(answer) == 0 or n == m:
                    n = m
                    answer.append(w)
            # m = max(len(w) for w in a)
            # if answer:
            #     if n == m:
            #         answer.update(a)
            #     elif n < m:
            #         n = m
            #         answer = set(a)
            # else:
            #     n = m
            #     answer.update(a)
        return answer

'''
Better solution would implement actual BFS and early terminate if it is
impossible to get any new answers (ie substring too short)
'''

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "()())()"
        o = sorted(["(())()","()()()"])
        self.assertEqual(sorted(s.removeInvalidParentheses(i)), o)

    def test_two(self):
        s = Solution()
        i = "(a)())()"
        o = sorted(["(a())()","(a)()()"])
        self.assertEqual(sorted(s.removeInvalidParentheses(i)), o)

    def test_three(self):
        s = Solution()
        i = ")("
        o = sorted([""])
        self.assertEqual(sorted(s.removeInvalidParentheses(i)), o)

    def test_four(self):
        s = Solution()
        i = "(()"
        o = sorted(["()"])
        self.assertEqual(sorted(s.removeInvalidParentheses(i)), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)