# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A string is a valid parentheses string (denoted VPS) if and only if it
    consists of "(" and ")" characters only, and:
    * It is the empty string, or
    * It can be written as AB (A concatenated with B), where A and B are VPS's
      or,
    * It can be written as (A), where A is a VPS.

    The nesting depth depth(S) is defined for any VPS S as follows:
    * depth("") = 0
    * depth(A+B) = max(depth(A), depth(B)), where A and B are VPS's
    * depth("(" + A + ")") = 1 + depth(A), where A is a VPS.

    Given a VPS sequence, split it into two disjoint subsequences A and B, such
    that A and B are VPS's (and A.length + B.length = sequence.length). The
    subsequences may not necessarily be contiguous.

    Choose any such A and B such that max(depth(A), depth(B)) is the minimum
    possible value.

    Return an answer array (of length seq.length) that encodes such a choice of
    A and B: answer[i] = 0 if seq[i] is part of A, else answer[i] = 1. Note that
    even though multiple answers may exist, return any of them. 
    '''
    def maxDepthAfterSplit_fails(self, seq: str) -> list[int]:
        n = len(seq)
        answer = [0] * n
        currA = True
        openA = 0
        openB = 0
        for i,j in enumerate(seq):
            if j == ')':
                if currA:
                    if openA > 0:
                        openA -= 1
                        answer[i] = 1
                    else:
                        openB -= 1
                        answer[i] = 0
                else:
                    if openB > 0:
                        openB -= 1
                        answer[i] = 0
                    else:
                        openA -= 1
                        answer[i] = 1
            else:
                if currA:
                    openA += 1
                else:
                    openB += 1
                answer[i] = 1 if currA else 0
                currA = not currA
        return answer

    # alternating currA does not capture correctly
    def maxDepthAfterSplit_fails(self, seq: str) -> list[int]:
        n = len(seq)
        answer = [8] * n
        stack = []
        currA = 0
        depth = 0
        for i,j in enumerate(seq):
            if j == '(':
                depth += 1
                stack.append((i,depth))
            else:
                x,d = stack.pop()
                depth -= 1
                answer[x] = answer[i] = currA
                if len(stack) == 0 or stack[-1][1] < d:
                    currA = 0 if currA == 1 else 1
        return answer

    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        n = len(seq)
        answer = [8] * n
        stack = []
        depth = 0
        for i,j in enumerate(seq):
            if j == '(':
                depth += 1
                stack.append(i)
            else:
                x = stack.pop()
                depth -= 1
                answer[x] = answer[i] = depth % 2
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "(()())"
        o = [0,1,1,1,1,0]
        self.assertEqual(s.maxDepthAfterSplit(i), o)

    def test_two(self):
        s = Solution()
        i = "()(())()"
        o = [0,0,0,1,1,0,1,1]
        self.assertEqual(s.maxDepthAfterSplit(i), o)

    def test_three(self):
        s = Solution()
        i = "(((())))"
        o = [0,1,0,1,1,0,1,0]
        self.assertEqual(s.maxDepthAfterSplit(i), o)

    def test_four(self):
        s = Solution()
        i = "((()(()((()()))((()()((()(()(()())(()(()))))))))))"
        o = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,1,1]
        self.assertEqual(s.maxDepthAfterSplit(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)