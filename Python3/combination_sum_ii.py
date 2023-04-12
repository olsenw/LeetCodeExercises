# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a collection of candidate numbers (candidates) and a target number
    (target), find all unique combinations in candidates where the candidate
    numbers sum to target.

    Each number in candidates may only be used once in the combination.

    Note the solution must not contain duplicate combinations.
    '''
    # derived from LeetCode solution
    # https://leetcode.com/problems/combination-sum-ii/editorial/
    # O(2^n) time O(n) space
    # nuts... have to track so much when backtracking
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        c = Counter(candidates)
        c = [(i, c[i]) for i in c]
        answer = []
        def bt(comb, remain, curr, counter, results):
            if remain == 0:
                results.append(list(comb))
                return
            elif remain < 0:
                return
            for next_curr in range(curr, len(counter)):
                candidate, freq = counter[next_curr]
                if freq <= 0:
                    continue
                comb.append(candidate)
                counter[next_curr] = (candidate, freq-1)
                bt(comb, remain - candidate, next_curr, counter, results)
                counter[next_curr] = (candidate, freq)
                comb.pop()
        bt([], target, 0, c, answer)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [10,1,2,7,6,1,5]
        j = 8
        o = [
            [1,1,6],
            [1,2,5],
            [1,7],
            [2,6]
            ]
        self.assertEqual(sorted(s.combinationSum2(i,j)), sorted(o))

    def test_two(self):
        s = Solution()
        i = [2,5,2,1,2]
        j = 5
        o = [
            [1,2,2],
            [5]
            ]
        self.assertEqual(sorted(s.combinationSum2(i,j)), sorted(o))

if __name__ == '__main__':
    unittest.main(verbosity=2)