# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an array of distint integers candidate, and a target integer
    target, return a list of all unique combinations of candidates where
    the chosen numbers sum to target. Combinations may be returned in
    any order.

    The same number may be chosen from candidate an unlimited number of
    times. Two combinations are unique if the frequency of at least one
    of the chosen numbers is different.

    It is guaranteed that the number of unique combinations that sum up
    to target is less than 150 combinations for the given input.
    '''
    # really slow... tuple frequency solution
    # forward facing solution... ie builds up to target (redundant work)
    # passes on leetcode however
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        # values reached by unique combinations
        # value -> set(tuple(frequency of candidate number))
        reach = {c:{tuple(1 if candidates[i] == c else 0 for i in range(len(candidates)))} for c in candidates}
        updates = candidates
        while updates:
            freshUpdates = set()
            for i in list(reach.keys()):
                for j in updates:
                    s = i + j
                    if s <= target:
                        freshUpdates.add(s)
                        frequencies = {tuple(a+b for a,b in zip(x,y)) for x in reach[i] for y in reach[j]}
                        if s in reach:
                            reach[s].update(frequencies)
                        else:
                            reach[s] = frequencies
            updates = freshUpdates
        pass
        if target not in reach:
            return []
        ans = []
        for r in reach[target]:
            a = []
            for i,j in enumerate(r):
                if j > 0:
                    a += [candidates[i]] * j
            ans.append(a)
        return ans

    # this is a backtracking solution using recursion 
    # written by nomofika (copied here for my reference/learning)
    # https://leetcode.com/problems/combination-sum/discuss/1777082/Python-Simple-backtracking-solution
    '''
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        
        ans = []
        def backtrack(i, s, comb):
            if i < 0:
                if s == target:
                    ans.append(comb)
                return
            
            if s + candidates[i] <= target:
                backtrack(i, s + candidates[i], comb + [candidates[i]])
            backtrack(i-1, s, comb)
        
        backtrack(n-1, 0, [])
        
        return ans
    '''

    # this is a backtracking solution without recursion 
    # written by Namangarg98 (copied here for my reference/learning)
    # https://leetcode.com/problems/combination-sum/discuss/918031/Python-beats-93-!!
    '''
    def combinationSum(self, candidates, target):
        dp = [[] for i in range(target+1)]
        
        for c in candidates:
            for i in range(target+1):
                if i<c: continue
                if i==c:
                    dp[i].append([c])
                else:
                    for blist in dp[i-c]:
                        dp[i].append(blist+[c])
        return dp[target]
    '''
class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,3,6,7]
        j = 7
        o = [[7],[2,2,3]]
        self.assertEqual(s.combinationSum(i,j), o)

    def test_two(self):
        s = Solution()
        i = [2,3,5]
        j = 8
        o = [[2,3,3],[3,5],[2,2,2,2]]
        self.assertEqual(s.combinationSum(i,j), o)

    def test_three(self):
        s = Solution()
        i = [2]
        j = 1
        o = []
        self.assertEqual(s.combinationSum(i,j), o)

    def test_four(self):
        s = Solution()
        i = [1,8]
        j = 9
        o = [[1]*9, [1,8]]
        self.assertEqual(s.combinationSum(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)