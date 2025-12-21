# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of n strings strs, all of the same length.

    Choose any deletion indices, and delete all the characters in those indices
    for each string.

    Suppose a set of deletion indices answer is chosen such that after
    deletions, the final array has elements in lexicographic order. Return the
    minimum possible value of answer.length.
    '''
    def minDeletionSize_fails(self, strs: List[str]) -> int:
        m = len(strs)
        n = len(strs[0])
        stack = [[0] * n for _ in range(m+1)]
        for j in range(n):
            last = strs[0][j]
            value = 0
            for i in range(1,m):
                if strs[i][j] < last:
                    value = 2
                    stack[i][j] = 2
                    break
                elif strs[i][j] == last:
                    value = max(value, 1)
                    stack[i][j] = 1
                last = strs[i][j]
            stack[m][j] = value
        answer = 0
        for j in range(n):
            if stack[m][j] == 0:
                break
            elif stack[m][j] == 2:
                answer += 1
        return answer

    # based on LeetCode editorial
    # https://leetcode.com/problems/delete-columns-to-make-sorted-ii/editorial/?envType=daily-question&envId=2025-12-21
    def minDeletionSize(self, strs: List[str]) -> int:
        # number of rows to toss
        answer = 0
        n = len(strs)
        # collected all columns
        cur = [""] * n
        for col in zip(*strs):
            # make a copy of cur
            cur2 = cur[:]
            # update as if keeping current column
            for i,l in enumerate(col):
                cur2[i] = cur2[i] + l
            # if lexicographical order, keep it
            if all(cur2[i] <= cur2[i+1] for i in range(len(cur2)-1)):
                cur = cur2
            else:
                answer += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["ca","bb","ac"]
        o = 1
        self.assertEqual(s.minDeletionSize(i), o)

    def test_two(self):
        s = Solution()
        i = ["xc","yb","za"]
        o = 0
        self.assertEqual(s.minDeletionSize(i), o)

    def test_three(self):
        s = Solution()
        i = ["zyx","wvu","tsr"]
        o = 3
        self.assertEqual(s.minDeletionSize(i), o)

    def test_four(self):
        s = Solution()
        i = ["abc","abc","abb"]
        o = 1
        self.assertEqual(s.minDeletionSize(i), o)

    def test_five(self):
        s = Solution()
        i = ["xga","xfb","yfa"]
        o = 1
        self.assertEqual(s.minDeletionSize(i), o)

    def test_six(self):
        s = Solution()
        i = ["xgga","xffb","yffa"]
        o = 2
        self.assertEqual(s.minDeletionSize(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)